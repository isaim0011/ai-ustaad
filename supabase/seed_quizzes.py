# seed_quizzes.py
# Comprehensive Roman Urdu Quizzes: 15 Modules x 5 Questions = Exactly 75 Questions Total

def get_quizzes():
    return [
        # =========================================================================
        # MODULE 0: Python Zero Se Hero (Prerequisite Track)
        # =========================================================================
        {
            "module_slug": "python-zero-se-hero",
            "title": "Module 0 Quiz: Python Foundations & Data Structures",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Python mein Mutable aur Immutable data types mein bunyadi farq kya hota hai?",
                    "options": [
                        "Lists aur Dictionaries mutable hain jabke Tuples aur Strings immutable hain",
                        "Tamam Python data types mutable hoti hain",
                        "Numbers mutable hote hain lekin Lists immutable",
                        "Python mein types compile-time par fix ho jati hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Python mein Lists, Sets aur Dictionaries mutable hain (unhe in-place modify kiya ja sakta hai), jabke Tuples, Integers, Floats aur Strings immutable hain (unhe in-place modify nahi kiya ja sakta, naya object banta hai)."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Classes mein `@dataclass(slots=True)` use karne ka sab se bara faida kya hota hai?",
                    "options": [
                        "Yeh dynamic `__dict__` overhead ko eliminate karke memory 20-30% save karta hai aur attribute lookup fast karta hai",
                        "Yeh class ko automatic PyTorch model bana deta hai",
                        "Yeh Python code ko Rust mein convert kar deta hai",
                        "Is se class mein methods add nahi kiye ja sakte"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "`slots=True` define karne se Python instance ke liye dictionary allocate karne ke bajaye fixed-size C array use karta hai, jisse memory usage kam hoti hai aur attribute access tez hota hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Expression `[x**2 for x in [1, 2, 3, 4] if x % 2 == 0]` ka final result kya hoga?",
                    "options": [
                        "[4, 16]",
                        "[1, 9]",
                        "[1, 4, 9, 16]",
                        "[2, 4]"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Yeh list comprehension sirf even numbers (2 aur 4) ko filter karti hai (`if x % 2 == 0`) aur unka square (2**2 = 4, 4**2 = 16) generate karti hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Functions mein `*args` aur `**kwargs` ka kya maqsad hota hai?",
                    "options": [
                        "`*args` positional arguments ko tuple mein aur `**kwargs` keyword arguments ko dictionary mein collect karta hai",
                        "`*args` sirf float numbers accept karta hai",
                        "`**kwargs` function ko asynchronous worker bana deta hai",
                        "Dono reserved keywords hain jo execute nahi ho sakte"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "`*args` (non-keyword arguments) ko tuple ke taur par aur `**kwargs` (keyword arguments) ko key-value pairs wali dictionary ke taur par function ke andar pass karta hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "JSON serialization ke waqt `json.dumps()` aur `json.dump()` mein kya farq hai?",
                    "options": [
                        "`json.dumps()` Python data ko string mein convert karta hai jabke `json.dump()` file handle mein write karta hai",
                        "`json.dumps()` database mein query execute karta hai",
                        "`json.dump()` sirf lists ke liye valid hai",
                        "Dono bilkul same function ke alias hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "`dumps` ka 's' String ke liye hai (serializes object to a JSON formatted str), jabke `dump()` pehla argument data aur doosra argument open file stream leta hai."
                }
            ]
        },
        # =========================================================================
        # MODULE 1: Python for AI & Fast Math
        # =========================================================================
        {
            "module_slug": "python-for-ai-and-fast-math",
            "title": "Module 1 Quiz: Python & Linear Algebra Check",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "NumPy mein Vectorized operations pure Python loops ke muqable mein kyun 50x se 100x tez hote hain?",
                    "options": [
                        "NumPy ke arrays C-contiguous memory blocks mein hote hain aur CPU SIMD instructions use karte hain",
                        "Python loops memory use nahi karte",
                        "NumPy hamesha GPU par run hota hai chahe CUDA na ho",
                        "NumPy code string format mein execute hota hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "NumPy ke arrays C-contiguous memory blocks mein hote hain aur modern CPU SIMD (Single Instruction Multiple Data) registers ka faida uthate hain, jabke Python loops mein har element generic object hota hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Agar do vectors u aur v ka Dot Product 0 ho, to iska geometrical matlab kya hai?",
                    "options": [
                        "Dono vectors bilkul identical hain",
                        "Dono vectors aapas mein 90 degree (orthogonal/perpendicular) hain",
                        "Dono vectors opposite directions mein hain",
                        "Dono vectors ki length zero hai"
                    ],
                    "correct_option_index": 1,
                    "explanation_roman_urdu": "Dot product formula u . v = |u| |v| cos(theta) hota hai. Jab angle 90 degree hota hai to cos(90) = 0, yaani dono vectors ek doosre se bilkul unrelated (orthogonal) hain."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Gradient Descent optimization mein Learning Rate parameter bohot zyada bara (high) rakhne se kya nuqsan ho sakta hai?",
                    "options": [
                        "Training foran 1 step mein complete ho jayegi",
                        "Model loss surface ke minimum ko overshoot kar dega aur loss diverge ho jayega",
                        "GPU memory full ho jayegi",
                        "Code syntax error de dega"
                    ],
                    "correct_option_index": 1,
                    "explanation_roman_urdu": "Bohot bara learning rate rakhne se parameters itni bari jump lagate hain ke wo minimum valley ko cross karke doosri taraf nikal jate hain aur loss function diverge (infinity ki taraf) ho jata hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Matrix Multiplication A @ B execute hone ke liye konsi mathematical shart lazmi hai?",
                    "options": [
                        "Dono matrices ka shape bilkul identical hona chahiye",
                        "Matrix A ke columns ki tadaad Matrix B ki rows ki tadaad ke barabar honi chahiye",
                        "Dono matrices square matrices honi chahiye",
                        "Matrix A ke elements positive hone chahiye"
                    ],
                    "correct_option_index": 1,
                    "explanation_roman_urdu": "Agar Matrix A ka dimension (m x k) ho, to Matrix B ka dimension lazmi (k x n) hona chahiye, taake inner dimension k match kare aur result (m x n) bane."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Eigenvalues aur Eigenvectors ka geometrical matlab kya hota hai?",
                    "options": [
                        "Transformation ke baad vector ki direction change nahi hoti, sirf scale (stretch ya shrink) hota hai",
                        "Vector hamesha 180 degree flip ho jata hai",
                        "Vector ki length hamesha zero ho jati hai",
                        "Matrix determinant zero ho jata hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "A * v = lambda * v formula ke mutabiq, eigenvector v par matrix A multiply karne se uski direction wahi rehti hai, sirf magnitude eigenvalue lambda se scale hota hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 2: Prompt Engineering & LLM Mental Models
        # =========================================================================
        {
            "module_slug": "prompt-engineering-and-llm-mental-models",
            "title": "Module 2 Quiz: Prompt Engineering & LLM Architecture",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "LLM generation ke waqt Temperature parameter ko 0.0 par set karne ka kya asar hota hai?",
                    "options": [
                        "Model bilkul random answers dega",
                        "Model hamesha highest probability wala token select karega (Greedy search/deterministic output)",
                        "Model ka context window 0 ho jayega",
                        "Model internet se live data fetch karega"
                    ],
                    "correct_option_index": 1,
                    "explanation_roman_urdu": "Temperature 0.0 softmax distribution ko sharpest kar deta hai jis se model hamesha sab se high probability token pick karta hai, deterministic aur consistent ban jata hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Chain-of-Thought (CoT) prompting complex reasoning tasks mein direct prompting se behtar kyun perform karti hai?",
                    "options": [
                        "CoT prompt model ko tokens generate karne ka waqt deta hai jisse intermediate computational steps execute hote hain",
                        "CoT se model ki training dubara shuru ho jati hai",
                        "CoT prompt sirf English mein kaam karta hai",
                        "CoT prompt token limit ko double kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "LLM ka computational budget directly generated tokens par depend karta hai. CoT model ko intermediate reasoning tokens generate karne par majboor karta hai jo final answer ke liye computation provide karte hain."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "System Prompt aur User Prompt mein Bunyadi farq kya hota hai?",
                    "options": [
                        "System prompt developer define karta hai jo model ka persona aur safety rules set karta hai, jabke user prompt end-user ki query hoti hai",
                        "System prompt sirf database mein save hota hai",
                        "System prompt hamesha user prompt ke baad execute hota hai",
                        "Dono bilkul aik jaisi cheez hain koi farq nahi"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "System prompt model ko guiding instructions, persona, constraints aur guardrails provide karta hai, jabke user prompt run-time query hoti hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Few-Shot Prompting mein kya technique use ki jati hai?",
                    "options": [
                        "Model ko prompt ke andar hi 2 se 5 concrete input-output examples provide ki jati hain",
                        "Model ko fine-tune kiya jata hai",
                        "Prompt ko 5 dafa repeat kiya jata hai",
                        "Model ke weights change kiye jate hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Few-shot prompting mein prompt ke context ke andar hi real examples di jati hain taake model pattern, output format aur style ko in-context learn kar sake."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Agar LLM Context Window limit (jaise 8k ya 32k tokens) exhaust ho jaye to kya hota hai?",
                    "options": [
                        "Pehle wale conversation tokens truncate ho jate hain aur model unhe bhool jata hai",
                        "Server physically restart ho jata hai",
                        "API automatically temperature barha deti hai",
                        "Output hamesha blank aata hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Context window exceed hone par shuru ke tokens attention mechanism se bahar nikal jate hain jis se model pehle di gayi context details bhool jata hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 3: Classical Machine Learning
        # =========================================================================
        {
            "module_slug": "classical-machine-learning",
            "title": "Module 3 Quiz: Classical ML & Scikit-Learn",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Machine Learning model mein Overfitting ka sab se bara symptom kya hota hai?",
                    "options": [
                        "Training data par bohot high accuracy (e.g. 99%) lekin Test/Validation data par bohot kharab accuracy",
                        "Model training hi na ho",
                        "Training data aur Test data dono par 50% accuracy",
                        "Model ka file size bohot chota ho jana"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Overfitting tab hoti hai jab model training data ke noise ko ratta laga leta hai, jis se unseen test data par generalization fail ho jati hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Random Forest algorithm kis ensemble technique par mabni hota hai?",
                    "options": [
                        "Bagging (Bootstrap Aggregating) of multiple Decision Trees",
                        "Single Linear Regression",
                        "Deep Convolutional Neural Network",
                        "K-Means Clustering"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Random Forest multiple decision trees ko data ke random subsets (bootstrap) par train karta hai aur unki predictions ka average ya majority vote leta hai (Bagging)."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "L1 Regularization (Lasso) aur L2 Regularization (Ridge) mein sab se ahem farq kya hai?",
                    "options": [
                        "L1 regularization non-important feature weights ko exactly ZERO kar deti hai (feature selection)",
                        "L2 regularization weights ko zero karti hai",
                        "L1 sirf classification mein use hoti hai",
                        "L2 mein training fast hoti hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "L1 penalty |w| gradients ko zero par push karti hai jis se sparse weights bante hain aur feature selection ho jati hai, jabke L2 penalty w^2 weights ko chota karti hai lekin zero nahi karti."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Medical Diagnosis jaise sensitive tasks mein Precision vs Recall mein se kis metric ko prioritize kiya jata hai?",
                    "options": [
                        "Recall ko, taake koi bhi bimaar mareez miss na ho (False Negatives minimize hon)",
                        "Precision ko, taake healthy mareez ko test na karna pare",
                        "Sirf Accuracy ko",
                        "Sirf training time ko"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Medical diagnosis mein False Negative khatarnak hota hai (bimaar ko healthy keh dena), is liye High Recall lazmi hoti hai taake tamam actual positive cases catch hon."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Distance-based algorithms (jaise KNN aur SVM) mein Feature Scaling (StandardScaler) kyun zaroori hoti hai?",
                    "options": [
                        "Taake bare scale wale features (jaise Salary 100,000) chote scale wale features (jaise Age 25) ko Euclidean distance mein overpower na karein",
                        "Data ko encrypt karne ke liye",
                        "Python errors prevent karne ke liye",
                        "Dataset ka size chota karne ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Euclidean distance direct numerical values par depend karti hai. Agar features normalize na hon to bara magnitude wala feature distance metric ko mukammal dominate kar leta hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 4: Deep Learning & PyTorch Core
        # =========================================================================
        {
            "module_slug": "deep-learning-and-pytorch-foundations",
            "title": "Module 4 Quiz: PyTorch Tensors & Neural Networks",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Neural Networks mein Activation Functions (jaise ReLU, GELU) add karna kyun lazmi hai?",
                    "options": [
                        "Non-linearity introduce karne ke liye, warna kitni bhi layers hon network ek simple linear regression ban kar reh jata hai",
                        "Memory consumption kam karne ke liye",
                        "Weights ko initialize karne ke liye",
                        "Data ko shuffle karne ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Agar non-linear activations na hon to W2 * (W1 * x) = (W2 * W1) * x = W_combined * x ban jata hai, yaani 100 layers bhi ek single linear transformation ban jati hain."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "PyTorch training loop mein `optimizer.zero_grad()` call karna kyun zaroori hota hai?",
                    "options": [
                        "Kyunke PyTorch by default gradients ko accumulate (add) karta hai, is liye har naye batch se pehle purane gradients clear karna lazmi hai",
                        "Weights ko reset karne ke liye",
                        "Learning rate ko zero karne ke liye",
                        "Loss function ko initialize karne ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "PyTorch mein `.backward()` previous gradients mein naye gradients add karta hai. Agar `.zero_grad()` na karein to multiple batches ke gradients jama ho kar weights ko corrupt kar denge."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "PyTorch mein `loss.backward()` method ka asal function kya hota hai?",
                    "options": [
                        "Autograd computation graph ke zariye chain rule apply karke tamam trainable parameters ke gradients compute karna",
                        "Loss ki value print karna",
                        "Model ko save karna",
                        "Weights ko update karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "`.backward()` reverse-mode automatic differentiation (backpropagation) execute karta hai aur har parameter ke `.grad` attribute mein gradient store karta hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Deep Sigmoid networks mein Vanishing Gradient Problem kyun paida hoti hai?",
                    "options": [
                        "Sigmoid derivative ka maximum value sirf 0.25 hota hai, deep layers mein multiply hote hote gradients zero ke qareeb pohanch jate hain",
                        "Sigmoid memory leak karta hai",
                        "Weights negative ho jate hain",
                        "Learning rate zero ho jati hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Sigmoid derivative hamesha 0 aur 0.25 ke darmiyan hota hai. 10 layers mein 0.25^10 = 0.00000095 ban jata hai, jis se initial layers ke weights train hona band ho jate hain."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Training ke doran `Dropout` layer neural network mein kya function perform karti hai?",
                    "options": [
                        "Randomly neurons ki activations ko zero kar deti hai taake neurons ek doosre par co-dependent na hon aur overfitting reduce ho",
                        "Corrupt data rows ko drop karti hai",
                        "Memory release karti hai",
                        "Model ki speed 2x karti hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Dropout regularizer hai jo training ke waqt randomly (e.g. 20% ya 50% probability par) neurons deactivate karta hai, jis se network robust representations seekhta hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 5: Attention & Transformers Under the Hood
        # =========================================================================
        {
            "module_slug": "attention-and-transformers-under-the-hood",
            "title": "Module 5 Quiz: Attention & Transformers Mechanics",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Self-Attention formula Softmax(Q * K^T / sqrt(d_k)) * V mein sqrt(d_k) se divide kyun kiya jata hai?",
                    "options": [
                        "Taake dot product magnitude bohot bara na ho jis se softmax gradients vanish ho jate hain",
                        "Computation speed ko double karne ke liye",
                        "Token length ko truncate karne ke liye",
                        "Matrix ko invertible banane ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Jab dimension d_k bara hota hai to dot product ka variance bara ho jata hai, jis se softmax outputs 0 ya 1 ke bohot qareeb ho jate hain aur gradients vanish ho jate hain. sqrt(d_k) scaling variance ko 1 rakhti hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Multi-Head Attention ka single attention head ke muqable mein kya faida hota hai?",
                    "options": [
                        "Model aik sath mukhtalif representation subspaces aur positions se information ko attend kar sakta hai (e.g. syntax, semantics, grammar)",
                        "Parameters 50% kam ho jate hain",
                        "Model ki inference latency zero ho jati hai",
                        "Transformers ko positional embeddings ki zaroorat nahi rehti"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Multi-head attention multiple independent projections use karta hai, jisse model ek head se subject-verb agreement aur doosre head se pronoun-reference track kar sakta hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Transformer models mein Positional Encoding add karna kyun lazmi hota hai?",
                    "options": [
                        "Kyunke Self-Attention mechanism permutation-invariant hota hai; bina positional encoding ke sentence mein lafzon ki tarteeb (order) lost ho jati hai",
                        "Model ke weights ko normalize karne ke liye",
                        "Context window barhane ke liye",
                        "Tokenization speed barhane ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Self-attention operations sets ki tarah order-independent hote hain. 'Billi ne sher ko dekha' aur 'Sher ne billi ko dekha' attention ke liye identical honge jab tak positional encoding add na ho."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Decoder-only models (jaise GPT aur Llama) mein Causal Attention Masking ka kya role hota hai?",
                    "options": [
                        "Future tokens ko -infinity mask kar deta hai taake model next token predict karte waqt aane wale tokens ko 'cheat' na kar sake",
                        "Prompt tokens ko delete kar deta hai",
                        "Gradients ko clip karta hai",
                        "Temperature ko scale karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Autoregressive models mein causal mask upper triangular matrix ko -inf kar deta hai taake softmax ke baad future positions ki attention weight 0 ho."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "LLM generation ke doran KV Cache (Key-Value Cache) use karne ka primary benefit kya hai?",
                    "options": [
                        "Pehle generate hone wale tokens ke Key aur Value tensors ko memory mein save rakhta hai taake har naye token par poora context dubara compute na karna pare",
                        "Model ka file size chota kar deta hai",
                        "Training time 10x fast kar deta hai",
                        "Accuracy ko 100% kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "KV cache bina use kiye N tokens generate karne mein O(N^2) computation lagti hai; KV cache save karne se har naye token par sirf naye token ka KV compute hota hai O(N)."
                }
            ]
        },

        # =========================================================================
        # MODULE 6: Building AI Applications & Modern APIs
        # =========================================================================
        {
            "module_slug": "building-ai-applications-and-apis",
            "title": "Module 6 Quiz: AI APIs & Streaming Architecture",
            "passing_score_pct": 70,
            "xp_reward": 25,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Server-Sent Events (SSE) streaming API endpoints ke liye konsa HTTP Content-Type header lazmi hota hai?",
                    "options": [
                        "text/event-stream",
                        "application/json",
                        "multipart/form-data",
                        "application/octet-stream"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "SSE ke liye `Content-Type: text/event-stream` header lazmi hota hai jo browser client ko batata hai ke HTTP connection open rahega aur data chunks push honge."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Client-side frontend mein AbortController use karne ka sab se bara faida kya hai?",
                    "options": [
                        "Jab user 'Stop Generating' click kare to active HTTP token stream foran abort ho jata hai jis se server aur token resources waste nahi hote",
                        "Network speed double ho jati hai",
                        "Response JSON format mein convert ho jata hai",
                        "Tokens automatically encrypt ho jate hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "AbortController ke `.abort()` signal se in-flight fetch request cancel ho jati hai aur backend stream generator close ho kar compute bacha leta hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "AI APIs mein Semantic Caching ka kya maqsad hota hai?",
                    "options": [
                        "Agar naya prompt purane cached prompt ke bohot qareeb ho (high cosine similarity) to direct cache se answer return karna bina LLM API call kiye",
                        "Images ko compress karna",
                        "SQL queries ko optimize karna",
                        "User passwords encrypt karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Semantic cache vector embeddings compare karta hai. 'Pakistan ka capital?' aur 'Capital of Pakistan?' par exact string match fail ho jata hai lekin vector cache 0.96 similarity par hit de kar $0 cost par instant answer serve karta hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "WebSockets aur Server-Sent Events (SSE) mein bunyadi farq kya hai?",
                    "options": [
                        "WebSockets full-duplex bidirectional (both ways) hote hain jabke SSE unidirectional (server-to-client) lightweight HTTP/2 stream hota hai",
                        "SSE sirf mobile par chalta hai",
                        "WebSockets JSON support nahi karte",
                        "Dono bilkul identical hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Text generation streams ke liye SSE behtareen hai kyunke simple HTTP connection use karta hai, jabke complex bidirectional audio/video ya tool chat ke liye WebSockets zaroori hote hain."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Sliding-Window Token Bucket rate limiter API gateway mein kya serve karta hai?",
                    "options": [
                        "API ko traffic bursts aur abuse se bachata hai taake downstream LLM quotas exhaust na hon aur fairness maintain rahe",
                        "Prompts ko translate karta hai",
                        "Responses ko grammar check karta hai",
                        "Token size double karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Token bucket rate limiting clients ko defined quota per minute assign karta hai aur DDoS ya excessive script requests ko 429 Too Many Requests status ke sath block karta hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 7: Vector Databases & Modern RAG
        # =========================================================================
        {
            "module_slug": "vector-databases-and-modern-rag",
            "title": "Module 7 Quiz: Vector Search & Hybrid RAG",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Hybrid Search mein Dense Retrieval aur Sparse Retrieval ko combine karne ka kya faida hota hai?",
                    "options": [
                        "Dense embeddings conceptual meaning capture karti hain jabke Sparse BM25 exact keywords, part numbers aur names match karta hai",
                        "Database ki RAM usage zero ho jati hai",
                        "Chunks ki zaroorat khatam ho jati hai",
                        "Accuracy hamesha 100% ho jati hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Sirf vector search exact serial numbers (e.g. 'ERR_404_B') par confuse ho sakti hai. Hybrid search Dense + BM25 ko Reciprocal Rank Fusion (RRF) se combine karke best of both worlds deti hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Cross-Encoder Re-ranker Bi-Encoder ke muqable mein behtar retrieval accuracy kyun deta hai?",
                    "options": [
                        "Cross-encoder query aur document tokens ko aik sath full self-attention se compare karta hai",
                        "Cross-encoder 100x fast hota hai",
                        "Cross-encoder vectors store nahi karta",
                        "Cross-encoder memory use nahi karta"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Bi-encoders query aur doc ko alag alag embed karte hain (fast candidate retrieval). Cross-encoder top 20 candidates ko query ke sath concatenate karke deep cross-attention se score karta hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Vector databases mein HNSW (Hierarchical Navigable Small World) index ka primary trade-off kya hai?",
                    "options": [
                        "Bohot fast sub-millisecond approximate nearest neighbor search milti hai lekin index building time aur RAM consumption zyada hoti hai",
                        "HNSW sirf 100 vectors store kar sakta hai",
                        "HNSW GPU ke baghair nahi chalta",
                        "HNSW mein vectors delete nahi ho sakte"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "HNSW multi-layer graph structure maintain karta hai jo O(log N) search latency provide karta hai lekin extra graph memory (RAM) demand karta hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "ColPali retrieval architecture traditional text OCR chunking ke muqable mein kyun superior hai?",
                    "options": [
                        "ColPali PDF pages ki images ko direct multi-vector Vision-Language representations mein index karta hai bina text extract kiye",
                        "ColPali sirf plain text documents read karta hai",
                        "ColPali vector database use nahi karta",
                        "ColPali training time zero karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Complex PDFs mein tables, charts aur layouts OCR mein mess up ho jate hain. ColPali visual embeddings se tables aur graphs ko as-is visually retrieve kar leta hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Text Chunking ke doran Chunks ke darmiyan Chunk Overlap (e.g. 50 tokens) rakhna kyun zaroori hota hai?",
                    "options": [
                        "Taake sentences ke darmiyan context split na ho aur boundary ke ahem information pieces lost na hon",
                        "Tokens count kam karne ke liye",
                        "File format maintain karne ke liye",
                        "Speed barhane ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Agar chunk boundary kisi zaroori sentence ke beech mein split ho jaye to dono chunks adhooray ho jate hain. Overlap boundary context ko preserve rakhta hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 8: Autonomous Agents & Tool Use
        # =========================================================================
        {
            "module_slug": "autonomous-agents-and-tool-use",
            "title": "Module 8 Quiz: Agents, MCP & Tool Use",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "ReAct (Reasoning + Acting) Agent framework ka core execution loop kya hota hai?",
                    "options": [
                        "Thought -> Action -> Action Input -> Observation -> Next Thought",
                        "Prompt -> Generate -> Exit",
                        "Input -> Database Query -> Output",
                        "Compile -> Run -> Debug"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "ReAct pattern mein agent pehle sochta hai (Thought), action decide karke tool call karta hai (Action), external world se result leta hai (Observation), aur phir agla step plan karta hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Anthropic Model Context Protocol (MCP) ka primary maqsad kya hai?",
                    "options": [
                        "AI models ko standardized open protocol ke zariye local files, tools, aur databases se connect karna",
                        "Naya transformer model train karna",
                        "CSS styles design karna",
                        "Python package manage karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "MCP ek open universal protocol hai (like USB-C for AI) jo AI models ko tools, prompts aur resources securely expose karta hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Multi-Agent Systems mein Supervisor / Router Pattern ka kya function hota hai?",
                    "options": [
                        "Ek coordinator agent user intent analyze karke specialized sub-agents (Coder, Researcher, Critic) ko kaam delegate karta hai",
                        "System crash prevent karta hai",
                        "Database backup leta hai",
                        "Token price calculate karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Supervisor pattern divide-and-conquer strategy use karta hai jahan main orchestrator sub-tasks create karta hai aur specialized agents unhe parallel execute karte hain."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Tool Use mein Function Calling ke waqt JSON Schema validation kyun critical hoti hai?",
                    "options": [
                        "Taake LLM se aane wale arguments ka type aur structure verify ho sake aur runtime code execution crashes prevent hon",
                        "Internet traffic kam karne ke liye",
                        "Model ko fast tokenize karne ke liye",
                        "Python syntax highlight karne ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "LLM kabhi kabhi invalid keys ya wrong data types generate kar sakta hai. Pydantic / JSON schema validate karke hallucinated parameters ko block karta hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Autonomous Agent mein Short-Term Memory aur Long-Term Memory mein kya farq hota hai?",
                    "options": [
                        "Short-term memory current context window scratchpad mein hoti hai, jabke long-term memory external vector database mein persist hoti hai",
                        "Short-term memory RAM mein hoti hai, long-term memory GPU mein",
                        "Dono identical hoti hain",
                        "Short-term memory expire nahi hoti"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Short-term memory current task execution context hoti hai jo session ke baad khatam ho sakti hai; long-term memory previous sessions ka persistent knowledge base hoti hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 9: Fine-Tuning & Model Adaptation
        # =========================================================================
        {
            "module_slug": "fine-tuning-and-model-adaptation",
            "title": "Module 9 Quiz: LoRA, Unsloth & DeepSeek-R1 GRPO",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "LoRA (Low-Rank Adaptation) mein rank parameter 'r' (e.g. r=16) ka kya role hota hai?",
                    "options": [
                        "Yeh low-rank decomposition matrices A aur B ke inner dimension ko control karta hai, jitna chota r utne kam trainable parameters",
                        "Yeh learning rate ko control karta hai",
                        "Yeh model ke total layers count ko barhata hai",
                        "Yeh GPU temperature ko fix karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "LoRA mein Delta W = B * A hota hai jahan A ka shape (r x d_in) aur B ka (d_out x r) hota hai. Rank r matrix compression ka bottleneck dimension hota hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "QLoRA mein NF4 (NormalFloat 4-bit) quantization format standard INT4 se behtar kyun hai?",
                    "options": [
                        "Normally distributed weights ke liye mathematically optimal quantile representation provide karta hai with near-zero accuracy loss",
                        "NF4 file size ko double kar deta hai",
                        "NF4 sirf AMD cards par chalta hai",
                        "NF4 training data ko encrypt karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Pre-trained neural network weights zero-mean normal distribution follow karte hain. NF4 quantization bins information theory ke mutabiq zero-loss mapping ensure karte hain."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "SFT (Supervised Fine-Tuning) dataset training ke waqt Loss Masking (-100 label) kyun lagai jati hai?",
                    "options": [
                        "Taake loss sirf assistant ke generated response tokens par calculate ho, system aur user prompt tokens par model train na ho",
                        "System prompt ko hide karne ke liye",
                        "Dataset se corrupt characters delete karne ke liye",
                        "GPU memory full hone se bachane ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Model ko user prompt memorize karne par penalize nahi karna chahiye. PyTorch CrossEntropyLoss label -100 ko ignore karta hai, so loss sirf assistant tokens par banti hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Direct Preference Optimization (DPO) traditional PPO RLHF se superior kyun mana jata hai?",
                    "options": [
                        "DPO ko separate Reward Model aur complex reinforcement learning loop ki zaroorat nahi hoti, direct policy probabilities se loss compute hoti hai",
                        "DPO sirf 10 parameters train karta hai",
                        "DPO bina GPU ke train hota hai",
                        "DPO training time 10x slow kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "DPO reward function ko mathematically substitute karke direct reference vs active policy log-likelihood ratios se train karta hai, jis se training crash-proof ban jati hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "DeepSeek-R1 ke GRPO (Group Relative Policy Optimization) mein Critic Model ki jagah kya cheez use hoti hai?",
                    "options": [
                        "Har prompt ke multiple sampled completions ka group mean aur standard deviation lekar normalized relative advantage calculate kiya jata hai",
                        "Ek bara 70B model judge banta hai",
                        "Human annotators live scoring karte hain",
                        "Zero reward assign kiya jata hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "GRPO Critic value-network ko eliminate karta hai. Group ke G candidate outputs ke rule-based rewards ka (r - mean) / std compute karke relative advantage derive hota hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 10: AI Safety, Evals & Guardrails
        # =========================================================================
        {
            "module_slug": "ai-safety-evals-and-guardrails",
            "title": "Module 10 Quiz: AI Evals & Safety Guardrails",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Ragas evaluation framework mein Faithfulness metric kis cheez ko mathematically measure karta hai?",
                    "options": [
                        "Generated answer ke claims kitne accurately retrieved context documents par grounded hain (Zero Hallucination check)",
                        "Answer kitna lamba hai",
                        "User prompt ki grammar check karna",
                        "API call ki latency measure karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Faithfulness score = (Number of claims in answer supported by context) / (Total claims in answer). 1.0 ka matlab zero hallucination hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "NeMo Guardrails mein Input Rails kis point par execute hoti hain?",
                    "options": [
                        "User query ko intercept karti hain aur LLM tak pohanchne se pehle jailbreaks aur malicious patterns block karti hain",
                        "LLM ke answer generate hone ke baad",
                        "Database save hone ke baad",
                        "Client browser band hone par"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Input rails gateway par pehli defense hoti hain jo adversarial prompt injections ko LLM inference se pehle hi drop kar deti hain, saving cost and securing the system."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Microsoft Presidio enterprise AI pipelines mein kya critical role ada karta hai?",
                    "options": [
                        "Personally Identifiable Information (PII) jaise CNIC, phone numbers, credit cards ko detect aur anonymize/mask karta hai",
                        "SQL queries generate karta hai",
                        "Images create karta hai",
                        "Model fine-tune karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Presidio sensitive personal details ko cloud LLM par bhejne se pehle replace karta hai (e.g. `<PAK_CNIC>`), ensuring GDPR and regulatory compliance."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "TruLens Groundedness evaluation kis Natural Language Inference (NLI) technique par kaam karta hai?",
                    "options": [
                        "Answer ke har sentence ko atomic claims mein split karke context ke sath entailment vs contradiction probability score karta hai",
                        "Word count ratio check karta hai",
                        "Alphabetical sorting karta hai",
                        "Cosine similarity calculate karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "TruLens NLI models (jaise DeBERTa) ke zariye check karta hai ke source text se answer logically entail (sabik) hota hai ya neutral/contradictory hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Automated CI/CD Evaluation Gates (DeepEval) software repository mein kyun lagaye jate hain?",
                    "options": [
                        "Taake agar naye prompt ya model change se accuracy ya safety benchmarks threshold se drop hon to PR merge automatically block ho jaye",
                        "Docker images delete karne ke liye",
                        "Developer ki salary deduct karne ke liye",
                        "Tests ko skip karne ke liye"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "DeepEval automated evaluation gates silent quality regressions ko production mein release hone se rokti hain by failing GitHub Actions workflows."
                }
            ]
        },

        # =========================================================================
        # MODULE 11: Production AI Engineering & MLOps
        # =========================================================================
        {
            "module_slug": "production-ai-engineering-mlops",
            "title": "Module 11 Quiz: vLLM, MLOps & High-Throughput Serving",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "vLLM serving engine ka PagedAttention algorithm traditional serving se kyun 10x-20x zyada throughput deliver karta hai?",
                    "options": [
                        "KV Cache ko contiguous memory mein rakhne ki bajaye non-contiguous virtual memory blocks mein page karta hai, eliminating memory waste and fragmentation",
                        "Model weights ko delete kar deta hai",
                        "Gradients ko zero kar deta hai",
                        "Sirf CPU par run hota hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "PagedAttention operating system ke virtual memory paging concept ko use karta hai. Har request ke liye dynamic blocks allocate hote hain jis se zero VRAM waste hoti hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Continuous Batching (Iteration-Level Scheduling) ka static batching ke muqable mein kya faida hai?",
                    "options": [
                        "Nayi incoming requests ko purani batch ke mukammal hone ka wait nahi karna parta; har token step par requests dynamically join aur leave kar sakti hain",
                        "Requests hamesha 1 by 1 process hoti hain",
                        "Batch size fixed 1 ho jati hai",
                        "Latency 10x barh jati hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Static batching mein fast requests ko slow requests ke finish hone ka wait karna parta tha. Continuous batching token-level scheduling se GPU utilization 95%+ rakhti hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "AWQ (Activation-aware Weight Quantization) ka fundamental technical insight kya hai?",
                    "options": [
                        "Sirf top 1% salient weights jin par activation magnitudes bohot bare hote hain unhe high-precision protect karna aur baqi 99% weights ko 4-bit quantize karna",
                        "Tamam weights ko random round off kar dena",
                        "Weights ko text format mein convert karna",
                        "Attention layers ko delete kar dena"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "AWQ activations ko observe karke ahem weights identify karta hai aur unhe mathematically scale karke protect karta hai, preserving reasoning accuracy."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Production LLM Streaming Gateways ke liye Rust Axum framework kyun choose kiya jata hai?",
                    "options": [
                        "Tokio async runtime ke zariye bina garbage collector pause ke 10,000+ concurrent SSE streams ko ultra-low CPU aur minimal RAM mein handle kar sakta hai",
                        "Rust mein code likhna Python se simple hota hai",
                        "Rust sirf GPUs par chalta hai",
                        "Rust automatic database banata hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Rust compile-time memory safety, zero-cost abstractions aur Tokio multi-threaded work-stealing scheduler high-concurrency streaming gateways ke liye industry benchmark hain."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Kubernetes par LLM inference clusters ko autoscale karte waqt KEDA autoscaler kis primary metric par scale out karta hai?",
                    "options": [
                        "vLLM Waiting Requests Queue Depth aur KV Cache Usage metrics par",
                        "Standard CPU percentage par",
                        "Disk storage usage par",
                        "Current clock time par"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "LLMs compute-bound aur memory-bound hote hain. GPU HPA autoscaling waiting queue depth par karni chahiye taake users ko latency spikes na milein."
                }
            ]
        },

        # =========================================================================
        # MODULE 12: Multimodal AI & Vision
        # =========================================================================
        {
            "module_slug": "multimodal-ai-and-vision",
            "title": "Module 12 Quiz: Multimodal AI & Vision-Language Models",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "OpenAI CLIP training mein InfoNCE Contrastive Loss ka primary objective kya hota hai?",
                    "options": [
                        "Matching (Image, Text) pairs ki cosine similarity ko matrix diagonal par maximize karna aur non-matching pairs ko zero ke qareeb push karna",
                        "Images ko 1000 classes mein classify karna",
                        "Images se background remove karna",
                        "Audio signals ko text mein convert karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "CLIP symmetric cross-entropy loss use karta hai jo shared embedding space mein positive image-text pairs ko aapas mein khinchti hai aur negative pairs ko dur karti hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Modern VLMs (jaise LLaVA) mein Cross-Modal Projector (MLP) ka kya role hota hai?",
                    "options": [
                        "Vision Encoder ke patch tokens ko LLM ke text embedding space (e.g. 1024-d to 4096-d) mein translate aur project karna",
                        "Image ka resolution 4k karna",
                        "Text prompt ko image mein badalna",
                        "Camera focus adjust karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Projector visual patch features ko LLM ke native token representations mein convert karta hai taake LLM ke attention layers unhe text tokens ki tarah seamlessly process kar sakein."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Visual Document Models (jaise Florence-2 aur Donut) classical OCR pipelines ke muqable mein kyun behtar hain?",
                    "options": [
                        "Direct visual pixels se spatial tables, forms aur layout structure ko Pydantic JSON mein parse karte hain bina brittle text-OCR preprocessing ke",
                        "Bohat zyada CPU memory use karte hain",
                        "Sirf English text read kar sakte hain",
                        "Files ko PDF mein convert karte hain"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "OCR-free visual document intelligence complex visual layout, dividing lines aur relative positioning ko visually samajh kar high-accuracy structured JSON generate karti hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "OpenAI Whisper speech recognition architecture mein raw audio signal ko pehle kis representation mein convert kiya jata hai?",
                    "options": [
                        "80-Channel Log-Mel Spectrogram (2D frequency-time representation)",
                        "MP3 compressed audio stream",
                        "Binary bitstream",
                        "RGB pixel matrix"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Audio wave ko Short-Time Fourier Transform (STFT) ke zariye human hearing sensitivity (Mel scale) par map kiya jata hai jo 2D Log-Mel spectrogram banata hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Long-form Video Understanding mein Uniform Keyframe Sampling (e.g. 1 frame per second) ka kya faida hai?",
                    "options": [
                        "Context window token consumption aur compute costs ko 95% reduce karta hai jabke primary temporal actions aur visual transitions retain rehte hain",
                        "Video ko slow-motion kar deta hai",
                        "Video ka audio mute kar deta hai",
                        "Video ko delete kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Har frame bhejenge to 30fps par hazaron redundant frames context window exhaust kar denge. Keyframe sampling critical state changes capture karti hai."
                }
            ]
        },

        # =========================================================================
        # MODULE 13: Local AI & Edge Devices
        # =========================================================================
        {
            "module_slug": "local-ai-and-edge-devices",
            "title": "Module 13 Quiz: Local LLMs, Ollama & Edge Optimization",
            "passing_score_pct": 70,
            "xp_reward": 30,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "llama.cpp mein GGUF binary format ka sab se bara faida kya hai?",
                    "options": [
                        "Single unified binary file jo OS mmap (memory mapping) ke zariye zero-copy instant load hoti hai aur CPU RAM par direct execute hoti hai",
                        "GGUF sirf Python mein execute hota hai",
                        "GGUF model ko uncompressed rakhta hai",
                        "GGUF file size ko 10x bara kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "GGUF metadata, vocabulary aur tensors ko single file mein pack karta hai jo memory-mapped I/O ke sath bina initial RAM loading lag ke instant token streaming provide karti hai."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Ollama Modelfile mein persistent persona aur guardrail instructions define karne ke liye konsi command use hoti hai?",
                    "options": [
                        "SYSTEM \"\"\"...\"\"\"",
                        "FROM base_model",
                        "PARAMETER temperature 0.7",
                        "TEMPLATE {{ .Prompt }}"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Modelfile mein `SYSTEM` command base model ke har conversation session ke liye permanent system prompt aur behavior boundaries enforce karti hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Apple Silicon (M1/M2/M3/M4) chips par LLM inference itni tez kyun hoti hai?",
                    "options": [
                        "Unified Memory Architecture (UMA) ki wajah se CPU aur GPU ek hi high-bandwidth memory pool (100GB/s se 800GB/s) zero-copy share karte hain",
                        "Apple devices par models train nahi hote",
                        "Apple chips internet use nahi karte",
                        "Apple chips mein cache memory nahi hoti"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Traditional PCs mein PCIe bus par VRAM transfer latency hoti hai. Apple Unified Memory mein weights direct RAM mein rehte hain aur Metal GPU instantly access karta hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "WebGPU aur Transformers.js ke zariye In-Browser AI chalane ka sab se bara business benefit kya hai?",
                    "options": [
                        "Zero backend server compute cost aur 100% airtight data privacy kyunke model direct user ke client browser mein execute hota hai",
                        "Browser ka tab crash ho jata hai",
                        "Client ko Python install karna parta hai",
                        "Internet traffic 10x barh jati hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Client-side WebGPU execution se SaaS company ko cloud GPU bills pay nahi karne parte aur user ka sensitive data kabhi browser se bahar nahi jata."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Embedded edge hardware (jaise Nvidia Jetson ya Raspberry Pi) par AI deploy karte waqt sab se ahem challenge kya hota hai?",
                    "options": [
                        "Strict power limits (e.g. 10W-15W budget) aur thermal throttling management taake device overheat ho kar crash na ho",
                        "Python versions ka match na hona",
                        "Monitor screen ka chota hona",
                        "Keyboard attach na hona"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Edge devices cooling aur power limited environments mein operate karte hain. Quantized models aur controlled inference frequencies thermal shutdowns prevent karti hain."
                }
            ]
        },

        # =========================================================================
        # MODULE 14: Enterprise Capstone & Career Launch
        # =========================================================================
        {
            "module_slug": "enterprise-capstone-and-career-launch",
            "title": "Module 14 Quiz: Enterprise Architecture & Career Capstone",
            "passing_score_pct": 70,
            "xp_reward": 50,
            "questions": [
                {
                    "question_number": 1,
                    "question_roman_urdu": "Enterprise multi-tenant systems mein PostgreSQL Row-Level Security (RLS) kya security guarantee provide karta hai?",
                    "options": [
                        "Database engine level par data isolate karta hai; agar application code mein WHERE clause miss bhi ho jaye to tenant kabhi doosre tenant ka data nahi dekh sakta",
                        "Database password encrypt karta hai",
                        "SQL injection ko allow karta hai",
                        "Backups automatically delete karta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "RLS policies database kernel level par har query par automatically `tenant_id = auth.jwt()->>'tenant_id'` inject karti hain, preventing cross-tenant data leaks."
                },
                {
                    "question_number": 2,
                    "question_roman_urdu": "Circuit Breaker pattern mein jab state 'OPEN' ho jaye to gateway ka kya behavior hota hai?",
                    "options": [
                        "Failing primary provider ko mazeed requests bhejna band kar deta hai aur foran secondary failover provider par traffic route karta hai",
                        "Tamam user requests ko drop kar deta hai",
                        "Server ko reboot kar deta hai",
                        "Database delete kar deta hai"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "OPEN circuit failing downstream service ko recover hone ka waqt deta hai aur instant failover ke zariye user requests ko 99.9% uptime ke sath serve karta hai."
                },
                {
                    "question_number": 3,
                    "question_roman_urdu": "Stripe Usage-Based Metered Billing integrate karne ka primary workflow kya hota hai?",
                    "options": [
                        "Har successful inference turn ke input aur output tokens count karke Stripe Meter Events API ko asynchronously report karna",
                        "User se har prompt par credit card CVV mangna",
                        "Monthly fixed bill generate karna bina usage track kiye",
                        "Stripe webhooks ko block karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Usage-based billing token consumption ke exact events Stripe billing meter ko bhejti hai jo month end par accurate consumption invoice generate karta hai."
                },
                {
                    "question_number": 4,
                    "question_roman_urdu": "Production packaging mein Multi-Stage Docker builds use karne ka kya faida hota hai?",
                    "options": [
                        "Heavy compilers aur build tools ko pehle stage mein chhor kar final image mein sirf lightweight compiled runtime binaries copy karna, reducing image size by 70%+",
                        "Docker image size 10GB bara kar dena",
                        "Deployment speed ko slow kar dena",
                        "Kubernetes ko bypass karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Multi-stage builds production containers ko minimal, secure aur fast banati hain. Attack surface minimize hoti hai aur deployment seconds mein execute hoti hai."
                },
                {
                    "question_number": 5,
                    "question_roman_urdu": "Global AI Engineering roles ($100k-$180k) secure karne ke liye sab se authentic proof-of-work kya hota hai?",
                    "options": [
                        "Live deployed public application URL, clear architectural diagrams, benchmark latency graphs aur open-source GitHub code",
                        "Sirf resume par buzzwords likhna",
                        "Certificates ki photos upload karna bina kisi working project ke",
                        "Theory questions yaad karna"
                    ],
                    "correct_option_index": 0,
                    "explanation_roman_urdu": "Global elite engineering teams working software, reproducible benchmarks aur clean system design ko dekhti hain. Live production projects are the ultimate unfair advantage."
                }
            ]
        }
    ]
