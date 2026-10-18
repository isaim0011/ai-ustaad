import os
import re
import subprocess
import sys
import urllib.parse

def get_pgpassword():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(base_dir, 'backend', '.env')
    with open(env_path, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'DATABASE_URL=postgresql://[^:]+:([^@]+)@', content)
    if not m:
        raise ValueError("Could not find password in DATABASE_URL")
    return urllib.parse.unquote(m.group(1))

def run_migrate(sql_files=None):
    pwd = get_pgpassword()
    env = os.environ.copy()
    env['PGPASSWORD'] = pwd
    migrate_js = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'migrate.js')
    args = ["node", migrate_js]
    if sql_files:
        args.extend(sql_files)
    res = subprocess.run(args, env=env, text=True, capture_output=True)
    print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    return res.returncode

if __name__ == '__main__':
    sql_files = sys.argv[1:]
    sys.exit(run_migrate(sql_files))
