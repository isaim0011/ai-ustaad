# module_03.py
# Module 3: Classical Machine Learning
# Lessons 3.1 to 3.6 rewritten with rigorous 4-part university-level structure.
# NO EMOJIS.

LESSON_CONTENT = {}

# ==============================================================================
# LESSON 3.1: Feature Engineering & Target Leakage
# ==============================================================================
LESSON_CONTENT['3.1'] = r"""### Part 1: Mental Model & South Asian Analogy
Aksar naye data scientists sochte hain ke machine learning ka jadu kisi complex algorithm (jaise XGBoost ya Neural Network) mein hota hai. Lekin dar-haqeeqat, machine learning ka 80% nateeja is baat par munhasir hota hai ke aapne raw data ko model ke qabil kaise banaya: yaani **Feature Engineering**!
Isay samajhne ke liye kisi Mashhoor Bawarchi (Chef) ki misaal lein:
1. Raw Data vs Prepared Ingredients: Farz karein aap bawarchi ke aage poori zinda murgi, mitti lagi hui sabut pyaz, aur sabut adrak phenk dein aur kahein "Zabardast Chicken Karahi banao". Bawarchi kabhi aisi cheezon ko direct handi mein nahi daal sakta. Pehle murgi ko saaf kiya jata hai, pyaz ko bareek kaata jata hai, aur adrak ko pees kar paste banaya jata hai (Feature Extraction & Transformation). Agar raw ingredient sahi tarah prepare na ho to behtareen se behtareen handi bhi zaiqa nahi de sakti.
2. Feature Scaling (Barabari Ka Wazan): Misaal lein tarazu ke do palron ki. Ek taraf customer ki tankhwah hai (PKR 150,000) aur doosri taraf customer ke bachon ki tadaad hai (2). Agar aap in dono numbers ko baghair scaling ke gradient descent model mein daalenge, to tankhwah ka number 150,000 itna haawi ho jayega ke bachon ki tadaad ka asar bilkul zero ho jayega! Standard Scaler dono numbers ko unke standard deviations ke mutabiq zero-mean aur unit-variance par lata hai taake tarazu barabar tol sake.
3. Target Leakage (Parchay Se Pehle Nateeja Maloom Hona): Yeh machine learning ka sab se khatarnak gunah hai. Misaal lein ek imtihan ki jahan master ji bache ki qabiliyat predict karna chahte hain, lekin ghalti se test paper ke bilkul oopar jawab ki answer key print kar dete hain. Bachay ke 100 mein se 100 number aate hain (Training Accuracy 100%). Lekin jab bacha asal board exam mein baithta hai to fail ho jata hai (Zero Generalization). Real world mein agar aap churn predict karte waqt 'account cancellation date' feature shamil kar lein to model cheat kar leta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Z-score Standardization (StandardScaler) ka riyazi hisab bilkul pehli bunyad se trace karein.
Formula for Z-score Standard Scaling:
$z = \frac{x - \mu}{\sigma}$
Jahan:
- $x$: Original feature value
- $\mu$: Feature column ka Arithmetic Mean (Average)
- $\sigma$: Feature column ka Standard Deviation

Numeric Dataset:
Customer Monthly Bills (in PKR): $[2000, 4000, 6000]$
Sample Count $N = 3$.

Step 1: Compute Mean ($\mu$)
$\mu = \frac{2000 + 4000 + 6000}{3} = \frac{12000}{3} = 4000.0$

Step 2: Compute Variance ($\sigma^2$) and Standard Deviation ($\sigma$)
$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$
- $(2000 - 4000)^2 = (-2000)^2 = 4,000,000$
- $(4000 - 4000)^2 = (0)^2 = 0$
- $(6000 - 4000)^2 = (2000)^2 = 4,000,000$
Sum of squared deviations $= 4,000,000 + 0 + 4,000,000 = 8,000,000$
$\sigma^2 = \frac{8,000,000}{3} \approx 2,666,666.67$
$\sigma = \sqrt{2,666,666.67} \approx 1632.99$

Step 3: Transform Each Value into Z-Score:
- $z_0 = \frac{2000 - 4000}{1632.99} = \frac{-2000}{1632.99} \approx -1.2247$
- $z_1 = \frac{4000 - 4000}{1632.99} = \frac{0}{1632.99} = 0.0000$
- $z_2 = \frac{6000 - 4000}{1632.99} = \frac{2000}{1632.99} \approx +1.2247$

Scaled Output Vector: $[-1.2247, 0.0000, +1.2247]$.
Naya Mean $\mu_z = 0.0000$ aur Naya Standard Deviation $\sigma_z = 1.0000$.
Ab chahe salary 1 lakh ho ya 1 crore, tamam features ek standard range mein aa kar model ko fast aur stable gradient descent dete hain.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum leak-free preprocessing pipeline implement karte hain: train-test split before scaling, One-Hot Encoding, missing value imputation, aur verification against target leakage.

```python
import numpy as np
import pandas as pd
from typing import Tuple

# 1. Create Synthetic Telco Churn Dataset
np.random.seed(42)
N_SAMPLES = 1000

raw_records = {
    "tenure_months": np.random.randint(1, 72, size=N_SAMPLES),
    "monthly_charges": np.random.uniform(500.0, 12000.0, size=N_SAMPLES),
    "contract_type": np.random.choice(["month_to_month", "one_year", "two_year"], size=N_SAMPLES),
    "churned": np.random.choice([0, 1], size=N_SAMPLES, p=[0.75, 0.25])
}

df = pd.DataFrame(raw_records)

# 2. Strict Train-Test Splitting BEFORE any feature processing (Guards against Data Leakage)
def train_test_split_manual(
    data: pd.DataFrame, 
    test_ratio: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices].copy(), data.iloc[test_indices].copy()

train_df, test_df = train_test_split_manual(df, test_ratio=0.2)
print(f"Train Shape: {train_df.shape} | Test Shape: {test_df.shape}")

# 3. Fit Scaler ONLY on Training Set
means = train_df[["tenure_months", "monthly_charges"]].mean()
stds = train_df[["tenure_months", "monthly_charges"]].std()

def transform_numerical_features(subset_df: pd.DataFrame) -> pd.DataFrame:
    scaled = subset_df[["tenure_months", "monthly_charges"]].copy()
    for col in ["tenure_months", "monthly_charges"]:
        scaled[col] = (scaled[col] - means[col]) / stds[col]
    return scaled

train_scaled = transform_numerical_features(train_df)
test_scaled = transform_numerical_features(test_df)

# 4. One-Hot Encoding with Training Set Vocabulary Guard
train_dummies = pd.get_dummies(train_df["contract_type"], prefix="contract", dtype=float)
# Re-index test set on train columns to prevent out-of-vocabulary mismatches
test_dummies = pd.get_dummies(test_df["contract_type"], prefix="contract", dtype=float)
test_dummies = test_dummies.reindex(columns=train_dummies.columns, fill_value=0.0)

# Combine Final Feature Tensors
X_train = np.hstack([train_scaled.values, train_dummies.values])  # Shape: [800, 5]
y_train = train_df["churned"].values                            # Shape: [800,]
X_test = np.hstack([test_scaled.values, test_dummies.values])    # Shape: [200, 5]
y_test = test_df["churned"].values                              # Shape: [200,]

print(f"X_train tensor shape: {X_train.shape} | X_test tensor shape: {X_test.shape}")
print(f"Train Scaled Mean (should be ~0.0): {train_scaled.mean().values.round(4)}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Fitting Scalers or Imputers on the Entire Dataset Before Splitting: Agar aap train-test split se pehle poore dataset par `scaler.fit_transform(X)` chalate hain to test set ki information (mean aur standard deviation) training set mein leak ho jati hai. Hamesha pehle split karein, phir train set par `.fit()`, aur test set par sirf `.transform()`.
2. Dummy Variable Trap (Multicollinearity): One-hot encoding karte waqt agar aap tamam $K$ categories ke naye columns rakhte hain to unka sum hamesha 1.0 hota hai, jo linear models mein matrix inversion error deta hai. Hamesha `drop_first=True` ya regularization use karein.
3. Imputing Missing Values with Global Constants Without Masking: Missing values ko 0 se fill karte waqt agar feature 'temperature' ya 'salary' ho to 0 ek valid value ban jati hai jo distribution ko distort karti hai. Median imputation ke sath `is_missing` boolean indicator column zaroor add karein.

Zero-GPU Tip:
Feature engineering, scaling, aur categorical encodings pure tabular math hain jo CPU par chalte hain. Scikit-learn aur NumPy ke zariye aap 10 lakh rows ka feature pipeline standard laptop CPU par 2 seconds mein transform kar sakte hain.

Self-Check Questions:
1. Target Leakage kya hai aur yeh model ke production performance ko kaise tabah karti hai?
2. Z-score Standardization aur Min-Max Normalization ($[0, 1]$) mein kya farq hai aur outliers hone par kaun sa behtar hai?
3. Test set par scaler fit kyun nahi kiya jata balki train set ka scaler transform kyun lagaya jata hai?

What to Build Next:
Ek Reusable Preprocessing Pipeline class banayein jo numerical columns ke mean/std aur categorical columns ke vocabulary levels ko `.fit(train_data)` mein save kare aur test records par `.transform(new_records)` execute kare."""

# ==============================================================================
# LESSON 3.2: Logistic Regression & Binary Cross-Entropy
# ==============================================================================
LESSON_CONTENT['3.2'] = r"""### Part 1: Mental Model & South Asian Analogy
Binary Classification (jaise: Customer chhor kar jayega ya nahi? Loan approve hoga ya reject?) ko samajhne ke liye kisi Bank ke Loan Officer ya Cricket Umpire ke faislay ki misaal lein:
1. Linear Regression vs Classification (Boundary Ka Masla): Farz karein aik bank ka loan officer kisi ki tankhwah aur credit score dekh kar faisla kar raha hai. Agar hum aam linear regression line use karein ($y = wx + b$), to ameer aadmi ke aane par model prediction 2.5 de dega aur ghareeb ke aane par -0.8 de dega! Lekin faisla to sirf 'Yes' (1) ya 'No' (0) mein hona hai. 2.5 probability ka kya matlab hai? Probability kabhi 0 se choti ya 1 se bari nahi ho sakti!
2. The Sigmoid Function (S-Shaped Squasher): Yahan kaam aati hai **Sigmoid Function**! Yeh aisi machine hai jo minus infinity se plus infinity tak ke kisi bhi baray number ko pakar kar $0.0$ aur $1.0$ ke darmiyan smooth 'S' curve mein squash (nichor) deti hai:
   - Agar score bara positive ho (e.g. $+5.0$), to Sigmoid $0.99$ (99% probability of approval) return karta hai.
   - Agar score bara negative ho (e.g. $-5.0$), to Sigmoid $0.01$ (1% probability) return karta hai.
   - Agar score bilkul darmiyan mein $0.0$ ho, to Sigmoid theek $0.50$ (50/50 uncertainty) deta hai.
3. Binary Cross-Entropy Loss (Ghalti Ki Saza): Farz karein ek cricket umpire 99% yaqeen ke sath kehta hai "Batsman Out hai!", lekin third umpire replay dekh kar Not Out de deta hai. Umpire ne na sirf ghalti ki, balki 99% confidence ke sath ghalti ki! Cross-Entropy loss aisi ghalti par exponentially shadeed tareen saza (Huge Penalty) lagati hai taake model ainda aisi ahmakana over-confident ghalti na kare.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Sigmoid calculation aur Binary Cross-Entropy (BCE) loss ka mukammal hisab step-by-step karein.
Formula for Sigmoid:
$\sigma(z) = \frac{1}{1 + e^{-z}}$

Formula for Binary Cross-Entropy (BCE) Loss:
$L = -\Big( y \log(\hat{y}) + (1 - y) \log(1 - \hat{y}) \Big)$
Jahan:
- $y \in \{0, 1\}$: True Ground Truth label
- $\hat{y} = \sigma(z)$: Predicted probability

Worked Numeric Scenario:
Single data sample:
- True label $y = 1$ (Customer Churned)
- Input feature $x = 1.5$
- Model Weight $w = 0.8$, Bias $b = -0.2$

Step 1: Compute Linear Logit ($z$)
$z = w \cdot x + b = (0.8 \times 1.5) + (-0.2) = 1.2 - 0.2 = 1.0$

Step 2: Pass Logit through Sigmoid
$\hat{y} = \sigma(1.0) = \frac{1}{1 + e^{-1.0}}$
$e^{-1.0} \approx 0.36788$
$\hat{y} = \frac{1}{1 + 0.36788} = \frac{1}{1.36788} \approx 0.73105$ (73.11% predicted probability)

Step 3: Compute Binary Cross-Entropy Loss
Kyunke $y = 1$, to second term $(1 - y) \log(1 - \hat{y})$ zero ho jati hai:
$L = -\Big( 1 \times \log_e(0.73105) + (1 - 1) \log_e(1 - 0.73105) \Big)$
$L = -\log_e(0.73105)$
Natural log: $\log_e(0.73105) \approx -0.31326$
$L = -(-0.31326) = 0.3133$

Compare with Severe Penalty Case:
Agar model $\hat{y} = 0.05$ (5% probability) predict karta jabke true label $y = 1$ tha:
$L = -\log_e(0.05) \approx 2.9957$ (Almost 10x higher loss)!
Ghalti jitni over-confident hogi, loss exponentially utna hi explode karega.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure NumPy ke sath vectorized Logistic Regression class, numerically-stable binary cross-entropy, aur gradient descent training loop from scratch implement karte hain.

```python
import numpy as np

class CustomLogisticRegression:
    \"\"\"Production-grade Logistic Regression from first principles in pure NumPy.\"\"\"
    def __init__(self, learning_rate: float = 0.1, n_iterations: int = 500) -> None:
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights: np.ndarray = np.array([])
        self.bias: float = 0.0

    @staticmethod
    def sigmoid(z: np.ndarray) -> np.ndarray:
        \"\"\"Numerically stable sigmoid preventing overflow on large positive/negative values.\"\"\"
        # Clip input to prevent overflow in exp(-z)
        z_clipped = np.clip(z, -50.0, 50.0)
        return 1.0 / (1.0 + np.exp(-z_clipped))

    def fit(self, X: np.ndarray, y: np.ndarray) -> list[float]:
        \"\"\"Trains model parameters via vectorized batch gradient descent.\"\"\"
        n_samples, n_features = X.shape
        # Initialize parameters
        self.weights = np.zeros(n_features, dtype=np.float32)
        self.bias = 0.0
        loss_history: list[float] = []

        for iteration in range(self.n_iterations):
            # 1. Forward Pass: compute logits and probabilities
            # Linear combination: z = Xw + b -> Shape: [n_samples]
            logits = np.dot(X, self.weights) + self.bias
            y_pred_prob = self.sigmoid(logits)

            # 2. Compute Binary Cross-Entropy Loss with stability epsilon
            eps = 1e-15
            y_prob_clipped = np.clip(y_pred_prob, eps, 1.0 - eps)
            bce_loss = -np.mean(y * np.log(y_prob_clipped) + (1.0 - y) * np.log(1.0 - y_prob_clipped))
            loss_history.append(float(bce_loss))

            # 3. Compute Analytical Gradients
            # Error residual: y_pred - y -> Shape: [n_samples]
            error = y_pred_prob - y
            dw = (1.0 / n_samples) * np.dot(X.T, error)  # Shape: [n_features]
            db = (1.0 / n_samples) * np.sum(error)        # Scalar

            # 4. Parameter Updates
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

        return loss_history

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        logits = np.dot(X, self.weights) + self.bias
        return self.sigmoid(logits)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X) >= threshold).astype(int)

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    # Synthetic linearly separable classification dataset
    X_syn = np.random.randn(200, 2).astype(np.float32)
    # Target rule: if x0 + 1.5 * x1 > 0 -> Class 1
    y_syn = ((X_syn[:, 0] + 1.5 * X_syn[:, 1]) > 0.0).astype(int)
    
    clf = CustomLogisticRegression(learning_rate=0.2, n_iterations=300)
    losses = clf.fit(X_syn, y_syn)
    
    predictions = clf.predict(X_syn)
    accuracy = np.mean(predictions == y_syn)
    print(f"Training Initial Loss: {losses[0]:.4f} -> Final Loss: {losses[-1]:.4f}")
    print(f"Model Learned Weights: {clf.weights.round(3)}, Bias: {clf.bias:.3f}")
    print(f"Classification Accuracy: {accuracy * 100:.1f}%")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Log of Absolute Zero in Cross-Entropy (`RuntimeWarning: divide by zero encountered in log`): Agar model kisi sample par $\hat{y} = 1.0$ ya $0.0$ predict kare to $\log(0)$ negative infinity ban jata hai aur poora loss `NaN` ho jata hai. Hamesha probabilities ko `np.clip(prob, 1e-15, 1.0 - 1e-15)` karein.
2. Hardcoding 0.5 Decision Threshold on Imbalanced Datasets: Agar fraud detection mein sirf 1% transactions fraudulent hon to 0.5 threshold par model hamesha zero fraud predict karega. Business risk ke mutabiq threshold ko 0.2 ya 0.1 par tune karna lazmi hai.
3. Exponent Overflow in Naive Sigmoid: $e^{-z}$ calculate karte waqt agar $z = -1000$ ho to $e^{1000}$ floating point overflow deta hai. `np.clip(z, -50, 50)` lagana zaroori hai.

Zero-GPU Tip:
Logistic regression aur Binary Cross-Entropy optimization matrix-vector dot products par chalte hain. 100,000 samples ka dataset kisi bhi basic CPU par 1 second se kam waqt mein train ho jata hai.

Self-Check Questions:
1. Linear regression aur Logistic regression ke output space mein kya farq hota hai?
2. Sigmoid function ki mathematical range kya hoti hai aur $z = 0$ par iski output value kya aati hai?
3. Binary Cross-Entropy loss over-confident ghalat predictions ko penalty kaise deti hai?

What to Build Next:
Ek Multi-Class Logistic Regression (Softmax Regression) classifier banayein jo 3 classes (e.g. Setosa, Versicolor, Virginica) ke darmiyan classification kare aur Categorical Cross-Entropy loss calculate kare."""

# ==============================================================================
# LESSON 3.3: Decision Trees & Random Forests
# ==============================================================================
LESSON_CONTENT['3.3'] = r"""### Part 1: Mental Model & South Asian Analogy
Linear models tab fail hote hain jab data ke darmiyan rishta seedha (linear) na ho, balki conditional rules par mushtamil ho. Yahan se shuru hota hai Tree-based algorithms ka aalam!
Isay samajhne ke liye kisi Khandani Rishta Karwane wali Khala (Matchmaker) aur Biradari ki Panchayat ki misaal lein:
1. Decision Tree (Rishta Wali Khala Ka Sawal-o-Jawab Flowchart): Jab rishta wali khala kisi larkay ka rishta dekhti hain to woh seedha gradient descent nahi chalateen. Woh ek zehni flowchart par chalti hain:
   - Root Node (Pehla Sawal): "Larka job karta hai ya be-rozgar hai?" Agar be-rozgar hai -> Seedha Reject (Leaf Node).
   - Internal Node (Doosra Sawal): Agar job karta hai -> "Salary 1 lakh se zyada hai ya kam?"
   - Leaf Node: Agar 1 lakh se zyada hai -> "Rishta Qabool!"
   Har node par ek conditional check hota hai jo data ko do hisson mein taqseem karta hai.
2. Gini Impurity (Doodh Mein Paani Ki Milawat): Decision Tree har step par aisa sawal kyun chun-ti hai? Khala aisa sawal dhoondti hain jo do groups ko bilkul saaf saaf alag kar de. Agar kisi group mein 50% larkay shareef hon aur 50% badmash hon to impurity sab se zyada (0.5) hoti hai. Agar kisi group mein 100% larkay shareef hon to impurity zero (0.0 - Pure Node) hoti hai. Tree hamesha wahi split chunti hai jo impurity ko sab se zyada kam kare!
3. Random Forest (Biradari Ki Panchayat): Ek akeli khala biased ho sakti hai ya kisi ek baat par hadd se zyada focus karke ghalat faisla kar sakti hai (Overfitting). Samajhdaar log kya karte hain? Woh 100 alag alag logon ki Panchayat (Ensemble) bithate hain. Har bande ko data ka alag random hissa (Bagging / Bootstrap Sampling) aur alag features dikhaye jate hain. Aakhir mein sab log vote daalte hain (Majority Voting). Panchayat ka faisla kisi ek fard ke faislay se 10 guna zyada robust aur reliable hota hai!

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Gini Impurity aur Information Gain ka exact hisab choti raqmon ke sath calculate karte hain.
Formula for Gini Impurity of a Node $S$:
$I_G(S) = 1 - \sum_{i=1}^{C} p_i^2$
Jahan $p_i$ class $i$ ka fraction (proportion) hai.

Dataset at Parent Node:
Total Candidates $N = 10$.
- Class 1 (Approved): 6 candidates ($p_1 = \frac{6}{10} = 0.6$)
- Class 0 (Rejected): 4 candidates ($p_0 = \frac{4}{10} = 0.4$)

Step 1: Compute Parent Gini Impurity
$I_G(\text{Parent}) = 1 - \Big( (0.6)^2 + (0.4)^2 \Big)$
$I_G(\text{Parent}) = 1 - (0.36 + 0.16) = 1 - 0.52 = 0.48$

Step 2: Evaluate a Candidate Split (Feature: "Salary > 50,000")
Farz karein is split se data do bachon (Left aur Right) mein taqseem ho jata hai:
Left Child ($N_L = 5$ candidates):
- 5 Approved, 0 Rejected ($p_1 = 1.0, p_0 = 0.0$)
$I_G(\text{Left}) = 1 - (1.0^2 + 0.0^2) = 1 - 1.0 = 0.0000$ (100% Pure Node!)

Right Child ($N_R = 5$ candidates):
- 1 Approved, 4 Rejected ($p_1 = \frac{1}{5} = 0.2, p_0 = \frac{4}{5} = 0.8$)
$I_G(\text{Right}) = 1 - (0.2^2 + 0.8^2) = 1 - (0.04 + 0.64) = 1 - 0.68 = 0.3200$

Step 3: Weighted Gini Impurity of the Split
$I_G(\text{Split}) = \frac{N_L}{N} I_G(\text{Left}) + \frac{N_R}{N} I_G(\text{Right})$
$I_G(\text{Split}) = \left(\frac{5}{10} \times 0.0\right) + \left(\frac{5}{10} \times 0.32\right) = 0.0 + 0.16 = 0.1600$

Step 4: Gini Gain (Impurity Reduction)
$\Delta I_G = I_G(\text{Parent}) - I_G(\text{Split}) = 0.48 - 0.16 = 0.3200$
Chunke Impurity mein $0.32$ ki zabardast kami aayi hai, Decision Tree algorithm is split ko approve kar deta hai!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum Decision Stump node split selector, recursive tree node structure, aur Random Forest bagging ensemble ko implement karte hain.

```python
import numpy as np
from typing import Optional, List, Tuple

class DecisionNode:
    \"\"\"Node container representing an internal condition split or leaf label.\"\"\"
    def __init__(
        self, 
        feature_index: Optional[int] = None, 
        threshold: Optional[float] = None, 
        left: Optional['DecisionNode'] = None, 
        right: Optional['DecisionNode'] = None, 
        value: Optional[int] = None
    ) -> None:
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value  # Leaf prediction value

    @property
    def is_leaf(self) -> bool:
        return self.value is not None

def compute_gini(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    p1 = np.mean(y == 1)
    p0 = 1.0 - p1
    return 1.0 - (p1**2 + p0**2)

def best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float, float]:
    \"\"\"Finds optimal feature index and threshold minimizing weighted Gini impurity.\"\"\"
    best_gain = -1.0
    best_feat = -1
    best_thresh = 0.0
    current_gini = compute_gini(y)
    n_samples, n_features = X.shape

    for feat_idx in range(n_features):
        thresholds = np.unique(X[:, feat_idx])
        for thresh in thresholds:
            left_mask = X[:, feat_idx] <= thresh
            right_mask = ~left_mask
            if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                continue

            g_left = compute_gini(y[left_mask])
            g_right = compute_gini(y[right_mask])
            weighted_gini = (np.sum(left_mask) / n_samples) * g_left + (np.sum(right_mask) / n_samples) * g_right
            gain = current_gini - weighted_gini

            if gain > best_gain:
                best_gain = gain
                best_feat = feat_idx
                best_thresh = float(thresh)

    return best_feat, best_thresh, best_gain

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    # 2 Features: [Monthly Spending in Thousands, Years Active]
    X_sample = np.array([
        [15.0, 1.0], [50.0, 3.0], [8.0, 0.5], [60.0, 4.0],
        [12.0, 2.0], [75.0, 5.0], [5.0, 0.2], [90.0, 2.5]
    ], dtype=np.float32)
    # Target: High Value Customer (1) or Churn Risk (0)
    y_sample = np.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=int)

    feat, thresh, gain = best_split(X_sample, y_sample)
    print(f"Optimal Root Split Found:")
    print(f"  Feature Index: {feat} (Feature {feat})")
    print(f"  Threshold:     {thresh:.2f}")
    print(f"  Gini Gain:     {gain:.4f} (Pure separation achieved!)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Growing Unconstrained Trees (Overfitting): Agar aap `max_depth` limit nahi lagate, to Decision Tree har akele training sample ke liye ek alag leaf bana leta hai (100% Train Accuracy, 50% Test Accuracy). Hamesha `max_depth=5` aur `min_samples_leaf=10` constraints lagayein.
2. In-Place Bootstrapping Bugs in Random Forest: Random Forest mein bagging karte waqt replacement sampling (`np.random.choice(N, size=N, replace=True)`) zaroori hoti hai. Agar `replace=False` kar dein to har tree ko bilkul aik jaisa data milta hai aur ensemble diversity khatam ho jati hai.
3. Ignoring High Cardinality Categorical Features: Agar kisi categorical column mein 10,000 unique values hon (jaise User ID), to Decision Tree us column par split karke fake perfect impurity reduction achieve kar leta hai jo test set par crash ho jati hai.

Zero-GPU Tip:
Decision Trees aur Random Forests CPU par embarrassing-parallel chalte hain. Scikit-learn ka `n_jobs=-1` parameter CPU ke tamam threads ko parallel activate karke 500 trees ko chund seconds mein train kar deta hai with zero GPU usage.

Self-Check Questions:
1. Gini Impurity aur Entropy mein kya farq hai aur dono node purity ko kaise measure karte hain?
2. Random Forest mein 'Bagging' (Bootstrap Aggregating) ka kya maqsad hai?
3. Out-Of-Bag (OOB) error score kya hota hai aur yeh cross-validation ka mutabadil kaise banta hai?

What to Build Next:
Ek Mini Random Forest Classifier banayein jo 10 bootstrap trees train kare, har tree ke liye random sub-features select kare, aur test samples par majority voting se prediction nikalay."""

# ==============================================================================
# LESSON 3.4: Gradient Boosted Trees: XGBoost & LightGBM Math
# ==============================================================================
LESSON_CONTENT['3.4'] = r"""### Part 1: Mental Model & South Asian Analogy
Kaggle competitions aur tabular production systems mein jo algorithm pichle 10 saal se badshah bana hua hai, uska naam hai **Gradient Boosted Decision Trees (GBDT)** jaise XGBoost aur LightGBM!
Isay samajhne ke liye kisi Cricket Team ke Head Coach aur Net Practice ki misaal lein:
1. Random Forest vs Boosting (Jamhooriyat vs Musalsal Islaah):
   - Random Forest aisi team hai jahan 11 alag alag players azadana practice karte hain aur aakhir mein sab ke scores ka average liya jata hai (Independent Parallel Voters).
   - Boosting ek ustaad aur shagird ka silsila hai jahan har naya player pichle player ki ghalti ko theek karne aata hai!
2. Learning from Residuals (Pichli Ghalti Ko Target Banana): Farz karein match jeetne ke liye 200 runs chahiye (Target $y = 200$).
   - Pehla Batsman (Tree 1) khelne jata hai aur 120 runs banata hai.
   - Ghalti (Residual / Error): $200 - 120 = 80$ runs abhi baqi hain!
   - Coach doosre batsman (Tree 2) se yeh nahi kehta ke "Tum 200 runs banao". Coach kehta hai: "Tumhara target sirf woh 80 runs hain jo pehla batsman nahi bana saka!"
   - Doosra batsman 50 runs banata hai. Naya Residual: $80 - 50 = 30$ runs!
   - Teesra batsman (Tree 3) sirf bache hue 30 runs ko target karta hai.
   Aakhir mein tamam batsmen ke runs jama ho kar theek 200 ban jate hain!
3. Second-Order Gradients (Hessians - XGBoost Ka Asli Asasa): Aam gradient boosting sirf yeh dekhti hai ke kis taraf jana hai (First Derivative / Gradient $g$). XGBoost yeh bhi dekhta hai ke road kitni rough hai aur dhalan kitni tez badal rahi hai (Second Derivative / Curvature / Hessian $h$). Iski wajah se XGBoost har step par behtareen step size khud calculate karta hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein XGBoost ke optimal leaf weight ($w^*$) aur Quality Score (Gain) ka exact formula calculate karte hain.
XGBoost Objective Function at a Leaf:
$\text{Obj} = \sum_{i \in I} \Big( g_i w + \frac{1}{2} (h_i + \lambda) w^2 \Big)$
Jahan:
- $g_i = \frac{\partial L}{\partial \hat{y}_i}$: First derivative (Gradient)
- $h_i = \frac{\partial^2 L}{\partial \hat{y}_i^2}$: Second derivative (Hessian)
- $\lambda$: L2 Regularization parameter
- $w$: Leaf output weight

Calculus se derivative zero karne par Optimal Leaf Weight nikalta hai:
$w^* = -\frac{\sum g_i}{\sum h_i + \lambda}$

Optimal Score (Split Quality Metric):
$S = -\frac{1}{2} \frac{(\sum g_i)^2}{\sum h_i + \lambda}$

Worked Numeric Example:
Single leaf jisme 3 samples hain:
Residuals (Gradients): $g_1 = -2.0, g_2 = -1.5, g_3 = -0.5$
Sum of gradients: $G = \sum g_i = -2.0 - 1.5 - 0.5 = -4.0$
Hessians for squared error loss ($h_i = 1.0$):
Sum of hessians: $H = \sum h_i = 1.0 + 1.0 + 1.0 = 3.0$
Regularization parameter: $\lambda = 1.0$

Step 1: Compute Optimal Leaf Weight $w^*$
$w^* = -\frac{G}{H + \lambda} = -\frac{-4.0}{3.0 + 1.0} = -\frac{-4.0}{4.0} = +1.0000$

Step 2: Compute Quality Score $S$
$S = \frac{1}{2} \frac{G^2}{H + \lambda} = \frac{1}{2} \frac{(-4.0)^2}{4.0} = \frac{1}{2} \frac{16.0}{4.0} = \frac{1}{2} \times 4.0 = 2.0000$
Jab tree split evaluate karta hai to woh check karta hai:
$\text{Gain} = S_{\text{Left}} + S_{\text{Right}} - S_{\text{Parent}} - \gamma$
Agar Gain positive ho to split accept hota hai, warna tree wahan ruk jata hai (Pruning)!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure NumPy ke sath First-Order Gradient Boosting Regressor (Residual Fitter) from scratch implement karte hain jo har step par decision stump train karke ensemble mein add karta hai.

```python
import numpy as np
from typing import List

class SimpleDecisionStump:
    \"\"\"1-level decision tree splitting on single feature threshold.\"\"\"
    def __init__(self) -> None:
        self.feature_idx: int = 0
        self.threshold: float = 0.0
        self.left_val: float = 0.0
        self.right_val: float = 0.0

    def fit(self, X: np.ndarray, residuals: np.ndarray) -> None:
        best_mse = float('inf')
        n_samples, n_features = X.shape

        for feat in range(n_features):
            thresholds = np.unique(X[:, feat])
            for thresh in thresholds:
                left_mask = X[:, feat] <= thresh
                right_mask = ~left_mask
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue

                val_l = float(np.mean(residuals[left_mask]))
                val_r = float(np.mean(residuals[right_mask]))

                pred = np.where(left_mask, val_l, val_r)
                mse = float(np.mean((residuals - pred) ** 2))

                if mse < best_mse:
                    best_mse = mse
                    self.feature_idx = feat
                    self.threshold = float(thresh)
                    self.left_val = val_l
                    self.right_val = val_r

    def predict(self, X: np.ndarray) -> np.ndarray:
        mask = X[:, self.feature_idx] <= self.threshold
        return np.where(mask, self.left_val, self.right_val)

class CustomGradientBoostedRegressor:
    \"\"\"Gradient Boosting Regressor fitting pseudo-residuals sequentially.\"\"\"
    def __init__(self, n_estimators: int = 20, learning_rate: float = 0.1) -> None:
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.base_pred: float = 0.0
        self.trees: List[SimpleDecisionStump] = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> List[float]:
        self.base_pred = float(np.mean(y))
        current_predictions = np.full_like(y, self.base_pred, dtype=np.float32)
        mse_history: List[float] = []

        for step in range(self.n_estimators):
            # Compute Residuals (Negative Gradient for MSE loss)
            residuals = y - current_predictions
            mse = float(np.mean(residuals ** 2))
            mse_history.append(mse)

            # Fit new tree to the residuals
            tree = SimpleDecisionStump()
            tree.fit(X, residuals)
            self.trees.append(tree)

            # Update ensemble predictions with shrinkage (learning rate)
            current_predictions += self.learning_rate * tree.predict(X)

        return mse_history

    def predict(self, X: np.ndarray) -> np.ndarray:
        preds = np.full(X.shape[0], self.base_pred, dtype=np.float32)
        for tree in self.trees:
            preds += self.learning_rate * tree.predict(X)
        return preds

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    # Synthetic non-linear data: y = sin(x) + noise
    X_toy = np.linspace(0.0, 6.0, 100).reshape(-1, 1).astype(np.float32)
    y_toy = np.sin(X_toy[:, 0]) + np.random.normal(0.0, 0.1, 100).astype(np.float32)

    gbr = CustomGradientBoostedRegressor(n_estimators=15, learning_rate=0.3)
    history = gbr.fit(X_toy, y_toy)

    print(f"Base Prediction (Mean): {gbr.base_pred:.4f}")
    print(f"Step 01 MSE: {history[0]:.4f} -> Step 15 MSE: {history[-1]:.4f}")
    print(f"Error Reduction: {((history[0] - history[-1]) / history[0]) * 100:.1f}%")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Setting High Learning Rate Without Enough Trees: Boosting mein `learning_rate = 0.5` rakhne se pehle 3 trees overfit kar jati hain aur aage seekhne ki gunjaish khatam ho jati hai. Production mein chota learning rate (`0.01` se `0.05`) aur zyada trees (`500` se `1000`) with Early Stopping behtareen standard hai.
2. Forgetting Tree Pruning with Gamma ($\gamma$): Agar aap tree ki splits par minimum gain requirement ($\gamma$) nahi lagate to tree bohot chote chote fuzool branches banata rehta hai jo sirf noise fit karte hain.
3. LightGBM vs XGBoost Memory Explosion on Dense Data: LightGBM histogram-based binning use karta hai jo 10x fast hota hai. XGBoost par agar aap `tree_method='exact'` use karenge to lakhoon rows par RAM khatam ho jayegi. Hamesha `tree_method='hist'` use karein.

Zero-GPU Tip:
LightGBM aur XGBoost ka Histogram mode (`hist`) CPU ke AVX2 registers ko itni efficiently use karta hai ke 1 crore rows ka tabular model 8-core CPU par 30 seconds mein train ho jata hai. GPU ki koi zaroorat nahi hoti jab tak data 50 GB se zyada na ho.

Self-Check Questions:
1. Random Forest (Bagging) aur Gradient Boosting mein bunyadi farq kya hai?
2. Boosting mein Shrinkage (Learning Rate) ka kya maqsad hai aur yeh overfitting ko kaise rokti hai?
3. XGBoost mein First Derivative ($g$) aur Second Derivative ($h$) ka formula optimal leaf weight kaise nikalta hai?

What to Build Next:
Ek Kaggle-Style Tabular Pipeline banayein jo LightGBM se telco churn predict kare, 5-Fold Stratified Cross-Validation use kare, aur ROC-AUC score print kare."""

# ==============================================================================
# LESSON 3.5: Model Evaluation: Precision, Recall, F1, ROC-AUC vs PR-AUC
# ==============================================================================
LESSON_CONTENT['3.5'] = r"""### Part 1: Mental Model & South Asian Analogy
Model train karne ke baad sab se bara dhoka evaluation metrics mein hota hai. Aam tor par log kehte hain: "Mere model ki Accuracy 99% hai!" Lekin production mein yeh 99% accuracy bilkul bekaar aur khatarnak ho sakti hai!
Isay samajhne ke liye Airport Security Scanner ya Dengue Test Laboratory ki misaal lein:
1. The Accuracy Paradox (99% Dhoka): Farz karein Karachi Airport par rozana 100,000 musafir aate hain. Inme se sirf 10 log terrorist ya smuggler hain (Imbalanced Data: 99.99% aam log hain). Agar security guard aakhein band karke so jaye aur har aane wale ko kahe "Jao jao sab theek hai!", to guard ki Accuracy 99.99% hogi! Lekin woh tamam 10 terrorists ko chhor dega. Is guard ki aisi 99.99% accuracy par usay nikal bahar phenkna chahiye!
2. Confusion Matrix Ke Chaar Pillar:
   - True Positive (TP): Smuggler aaya aur pakra gaya (Kamyabi).
   - True Negative (TN): Sharif aadmi aaya aur baghair tang kiye jane diya gaya (Kamyabi).
   - False Positive (FP - Type I Error): Sharif aadmi par ghalat shuba karke use 4 ghantay jail mein baitha diya (Be-gunaah ko saza).
   - False Negative (FN - Type II Error): Smuggler hathiyar le kar security se nikal gaya (Fatal Disaster)!
3. Precision vs Recall:
   - Precision (Khaalis-pan): "Jab guard ne kisi ko chor kaha, to unme se waqai kitne chor niklay?" ($TP / (TP + FP)$). High precision zaroori hai spam detection mein taake koi ahem email junk mein na jaye.
   - Recall (Pakarne Ki Quwwat): "Total kitne chor aaye the aur guard unme se kitne pakar saka?" ($TP / (TP + FN)$). High recall zaroori hai cancer ya dengue test mein kyunke hum kisi mareez ko miss nahi kar sakte chahe chund healthy logon ka dobara test hi kyun na karna paray!
4. ROC-AUC vs PR-AUC: Jab dataset bohot imbalanced ho (jaise fraud ya disease), to ROC curve jhooti tasweer dikhati hai kyunke usme True Negatives bohot zyada hote hain. Aise cases mein Precision-Recall AUC (PR-AUC) hamesha haqeeqi performance ka aaina hota hai.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Confusion Matrix se tamam ahem metrics ka hisab step-by-step concrete numbers ke sath karein.
Test Dataset: 100 Patients tested for rare disease.
- True Positives ($TP$) = 8 (Waqai beemar the aur model ne detect kar liya)
- False Negatives ($FN$) = 2 (Beemar the lekin model ne kaha healthy hain)
- False Positives ($FP$) = 10 (Healthy the lekin model ne ghalti se alert bajaya)
- True Negatives ($TN$) = 80 (Healthy the aur model ne correctly clear kiya)

Step 1: Compute Accuracy
$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{8 + 80}{8 + 80 + 10 + 2} = \frac{88}{100} = 88.0\%$

Step 2: Compute Precision
$\text{Precision} = \frac{TP}{TP + FP} = \frac{8}{8 + 10} = \frac{8}{18} \approx 0.4444$ (44.44%)
Iska matlab jab model beemari ka shuba karta hai, to sirf 44% martaba baat sach hoti hai.

Step 3: Compute Recall (Sensitivity)
$\text{Recall} = \frac{TP}{TP + FN} = \frac{8}{8 + 2} = \frac{8}{10} = 0.8000$ (80.0%)
Model ne 80% mareezon ko pakar liya, lekin 20% mareez miss ho gaye.

Step 4: Compute F1-Score (Harmonic Mean of Precision and Recall)
Aam average (Arithmetic Mean) is liye use nahi hoti kyunke agar Precision 0 ho to F1 ko zero hona chahiye:
$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$
$F_1 = 2 \times \frac{0.4444 \times 0.8000}{0.4444 + 0.8000} = 2 \times \frac{0.3555}{1.2444} = 2 \times 0.2857 = 0.5714$
Dekhein! Accuracy 88% thi, lekin asal F1 score sirf 57% hai! Yeh farq production model ki kamyabi aur nakami ka faisla karta hai.

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum pure NumPy ke sath complete confusion matrix, precision, recall, F1-score, aur dynamic decision threshold sweeping PR-curve calculator implement karte hain.

```python
import numpy as np
from typing import Dict, Tuple

def compute_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, int]:
    \"\"\"Calculates fundamental confusion matrix quadrants.\"\"\"
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}

def evaluate_classification_metrics(y_true: np.ndarray, y_pred_prob: np.ndarray, threshold: float = 0.5) -> Dict[str, float]:
    \"\"\"Computes precision, recall, F1, and balanced accuracy at specific decision boundary.\"\"\"
    y_pred = (y_pred_prob >= threshold).astype(int)
    cm = compute_confusion_matrix(y_true, y_pred)
    
    tp, tn, fp, fn = cm["TP"], cm["TN"], cm["FP"], cm["FN"]
    eps = 1e-9

    accuracy = (tp + tn) / max(tp + tn + fp + fn, 1)
    precision = tp / max(tp + fp, eps)
    recall = tp / max(tp + fn, eps)
    f1 = 2 * (precision * recall) / max(precision + recall, eps)

    return {
        "threshold": threshold,
        "TP": tp, "FP": fp, "FN": fn, "TN": tn,
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4)
    }

# Execution test
if __name__ == "__main__":
    np.random.seed(42)
    # Simulate imbalanced fraud detection test set (5% fraud)
    N_TEST = 1000
    y_ground_truth = np.random.choice([0, 1], size=N_TEST, p=[0.95, 0.05])
    
    # Model generates realistic calibrated probabilities
    # Positive samples get higher average scores with some noise
    y_scores = np.where(
        y_ground_truth == 1, 
        np.random.beta(5, 2, size=N_TEST), 
        np.random.beta(1, 4, size=N_TEST)
    )

    print("--- Evaluating Decision Threshold Tradeoffs ---")
    for thresh in [0.2, 0.5, 0.8]:
        metrics = evaluate_classification_metrics(y_ground_truth, y_scores, threshold=thresh)
        print(f"Threshold {thresh:.1f} -> Precision: {metrics['precision']:.3f} | Recall: {metrics['recall']:.3f} | F1: {metrics['f1_score']:.3f}")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Optimizing for Accuracy on Severe Class Imbalance: Fraud detection ya ad click-through rate jaise 99:1 imbalanced problems par accuracy check karna sab se bara novice blunder hai. Aise cases mein hamesha PR-AUC aur F1-Score ko optimization metric banayein.
2. Mixing Up False Positives with False Negatives: Medical diagnosis mein False Negative (cancer mareez ko kehna aap theek hain) jaan leva hota hai, jabke False Positive sirf ek extra biopsy mangta hai. Metric chunne se pehle business cost of error lazmi define karein.
3. Calculating Metrics on the Training Set: Training set par evaluation metrics nikal kar report banana overfitted model ko perfect dikhata hai. Metrics hamesha unseen Out-Of-Fold ya Held-Out Test set par report karein.

Zero-GPU Tip:
Evaluation metrics, confusion matrices, aur ROC/PR curves calculate karna purely analytical CPU math hai. 10 lakh predictions ka threshold sweep NumPy par 15 milliseconds mein execute ho jata hai.

Self-Check Questions:
1. Accuracy Paradox kya hota hai aur imbalanced data par yeh kyun dhoka deta hai?
2. F1-Score mein Arithmetic Mean ke bajaye Harmonic Mean kyun use ki jati hai?
3. ROC-AUC aur Precision-Recall AUC (PR-AUC) mein kya farq hai aur fraud detection mein kaun sa behtar hai?

What to Build Next:
Ek Automated Threshold Optimizer banayein jo $0.05$ se $0.95$ tak tamam thresholds sweep kare aur business profit matrix ($+\$100$ per TP, $-\$20$ per FP, $-\$500$ per FN) ke mutabiq optimal threshold nikalay."""

# ==============================================================================
# LESSON 3.6: Module 3 Capstone: Production Churn Prediction Service
# ==============================================================================
LESSON_CONTENT['3.6'] = r"""### Part 1: Mental Model & South Asian Analogy
Mubarak ho! Aapne Classical Machine Learning ke tamam foundational sutoon (Feature engineering, Logistic regression math, Decision trees, XGBoost boosting math, aur Imbalanced evaluation metrics) mukammal kar liye hain. Ab waqt hai is tamam ilm ko ek **Production-Grade Churn Prediction Microservice** mein tabdeel karne ka!
Is Capstone project ka zehni khaka kisi Bare Telecom Network (Jaise Jazz, Zong, ya Telenor) ke Retention Department jaisa hai:
1. Daily Customer Usage Feed: Rozana raat ko lakhon mobile users ka data system mein aata hai: kisne kitne call minutes use kiye, kitna internet data kharch kiya, aur kitni dafa complaint call ki.
2. The Churn Scorer (Inference Engine): Customer service ke bande ke aage ek real-time dashboard hota hai. Jab koi customer call center par phone karta hai to system foran us customer ka feature vector nikalta hai, pre-trained model se probability score calculate karta hai, aur screen par alert dikhata hai: "Risk Score: 85% - High Churn Risk!"
3. Automated Retention Action (Business Strategy): Agar score 80% se zyada ho to call center agent ko prompt milta hai: "Is customer ko 20% discount offer karein taake yeh doosre network par port out na kare."
4. REST API Contract: Yeh service ek fast, robust FastAPI/Pydantic web endpoint ke taur par chalni chahiye jo millisecond latency par JSON request le kar structured prediction return kare.

### Part 2: First-Principles Logic & Worked Numeric Example
Aayein Churn Risk Scoring aur Threshold Decision Rule ka complete hisab step-by-step trace karte hain.
Trained Model Coefficients (Logistic Regression Baseline):
Features:
- $x_0$: `tenure_months` (Scaled Z-score)
- $x_1$: `monthly_charges` (Scaled Z-score)
- $x_2$: `num_complaints` (Scaled Z-score)
- $x_3$: `contract_month_to_month` (Binary 0 or 1)

Learned Weights:
$w = [-0.60, +0.40, +0.85, +1.20]$
Bias $b = -0.50$

Customer Profile (Incoming Call):
Customer Raw Data:
- Tenure = 4 months (Low loyalty -> Scaled $x_0 = -1.2$)
- Monthly Bill = 3500 PKR (High bill -> Scaled $x_1 = +0.8$)
- Complaints in last month = 3 (Very frustrated -> Scaled $x_2 = +2.0$)
- Contract = Month-to-Month ($x_3 = 1.0$)

Step 1: Compute Linear Logit ($z$)
$z = (w_0 x_0) + (w_1 x_1) + (w_2 x_2) + (w_3 x_3) + b$
$z = (-0.60 \times -1.2) + (0.40 \times 0.8) + (0.85 \times 2.0) + (1.20 \times 1.0) - 0.50$
$z = 0.72 + 0.32 + 1.70 + 1.20 - 0.50$
$z = 3.44$

Step 2: Compute Churn Probability via Sigmoid
$P(\text{Churn}) = \sigma(3.44) = \frac{1}{1 + e^{-3.44}}$
$e^{-3.44} \approx 0.03206$
$P(\text{Churn}) = \frac{1}{1 + 0.03206} = \frac{1}{1.03206} \approx 0.9689$ (96.89% Probability)!

Business Decision Rule:
- $P \ge 0.75 \implies$ High Risk: Trigger "Urgent Retention Retention Call + 25% Discount Voucher".
Customer flagged immediately with actionable business outcome!

### Part 3: Annotated Production Code
Neeche diye gaye production code mein hum end-to-end production churn inference service implement karte hain: strict Pydantic input/output schemas, feature scaling persistence, model prediction, aur latency tracking.

```python
import json
import time
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field

# 1. Strict Input Schema
class CustomerInferencePayload(BaseModel):
    customer_id: str = Field(min_length=3, max_length=20)
    tenure_months: int = Field(ge=0, le=120)
    monthly_charges: float = Field(ge=0.0, le=50000.0)
    num_complaints: int = Field(ge=0, le=50)
    is_month_to_month: bool

# 2. Strict Output Schema
class ChurnPredictionResponse(BaseModel):
    customer_id: str
    churn_probability: float = Field(ge=0.0, le=1.0)
    risk_level: Literal["low", "medium", "high"]
    recommended_action: str
    latency_ms: float

# 3. Production Model Artifact Wrapper
class ProductionChurnService:
    def __init__(self) -> None:
        # Pre-calculated training distribution statistics for scaling
        self.stats = {
            "tenure_mean": 24.0, "tenure_std": 15.0,
            "charges_mean": 2000.0, "charges_std": 1200.0,
            "complaints_mean": 0.5, "complaints_std": 0.8
        }
        # Pre-trained logistic model weights
        self.weights = [-0.60, 0.40, 0.85, 1.20]
        self.bias = -0.50

    def predict_single(self, payload: CustomerInferencePayload) -> ChurnPredictionResponse:
        t0 = time.perf_counter()

        # 1. Feature Standardization using frozen training statistics
        x0 = (payload.tenure_months - self.stats["tenure_mean"]) / self.stats["tenure_std"]
        x1 = (payload.monthly_charges - self.stats["charges_mean"]) / self.stats["charges_std"]
        x2 = (payload.num_complaints - self.stats["complaints_mean"]) / self.stats["complaints_std"]
        x3 = 1.0 if payload.is_month_to_month else 0.0

        # 2. Compute Logit and Sigmoid
        logit = (self.weights[0] * x0) + (self.weights[1] * x1) + (self.weights[2] * x2) + (self.weights[3] * x3) + self.bias
        # Safe Sigmoid
        clipped_logit = max(min(logit, 50.0), -50.0)
        prob = 1.0 / (1.0 + (2.718281828459045 ** (-clipped_logit)))
        prob = round(float(prob), 4)

        # 3. Business Decision Rules
        if prob >= 0.75:
            risk = "high"
            action = "Dispatch 25% Loyalty Retention Discount Voucher immediately"
        elif prob >= 0.40:
            risk = "medium"
            action = "Queue for customer satisfaction feedback survey"
        else:
            risk = "low"
            action = "Eligible for upsell premium add-on package"

        elapsed_ms = round((time.perf_counter() - t0) * 1000.0, 3)

        return ChurnPredictionResponse(
            customer_id=payload.customer_id,
            churn_probability=prob,
            risk_level=risk,
            recommended_action=action,
            latency_ms=elapsed_ms
        )

# Execution test
if __name__ == "__main__":
    service = ProductionChurnService()

    # Test High-Risk Customer
    payload_high_risk = CustomerInferencePayload(
        customer_id="CUST_PK_901",
        tenure_months=3,
        monthly_charges=3800.0,
        num_complaints=4,
        is_month_to_month=True
    )

    response = service.predict_single(payload_high_risk)
    print("Inference Successful!")
    print(f"Customer: {response.customer_id}")
    print(f"Churn Probability: {response.churn_probability * 100:.2f}%")
    print(f"Risk Tier: {response.risk_level.upper()}")
    print(f"Action: {response.recommended_action}")
    print(f"Inference Latency: {response.latency_ms} ms (Real-time production SLA)")
```

### Part 4: Common Mistakes, Zero-GPU Tips, Self-Check & Next Challenge
Common Mistakes:
1. Hardcoding Scaler Values Directly into Code Without Model Versioning: Training set ki distribution badalti rehti hai. Production mein scaler parameters aur model weights ko hamesha versioned artifact file (jaise JSON ya ONNX) se load karna chahiye.
2. Silent Type Coercion Bugs on Inputs: Agar API user `tenure_months="three"` string bhej de aur schema validation na ho to string calculation crash kar deti hai. Pydantic schema validation lagana lazmi hai.
3. Lack of Inference Latency Telemetry: Agar prediction endpoint par telemetry na ho to network bottleneck ya slow database lookups ka pata nahi chalta. Hamesha per-request latency monitor karein.

Zero-GPU Tip:
Tabular ML inference CPU par microseconds mein chalti hai. Is microservice ko aap kisi bhi free Cloud Run ya container environment par 0.1 vCPU ke sath host kar sakte hain jo hazaron requests per second serve kar sakti hai.

Self-Check Questions:
1. Feature scaling ke statistics (`mean` aur `std`) production inference ke waqt kahan se aate hain?
2. Sigmoid function ki output probability ko business action mein convert karne ke liye threshold kaise chuna jata hai?
3. Production ML service mein Pydantic input validation ka kya faida hai?

What to Build Next:
Is Churn Prediction Service ko ek live FastAPI app mein wrap karein with a `/predict` POST endpoint, aur batch prediction endpoint `/predict-batch` support karein."""
