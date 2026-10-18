import os
import sys
import subprocess
import run_migration

def run_query(sql):
    pwd = run_migration.get_pgpassword()
    env = os.environ.copy()
    env['PGPASSWORD'] = pwd
    node_code = f"""
const {{ Client }} = require('pg');
(async () => {{
  const c = new Client({{
    host: 'aws-0-ap-southeast-1.pooler.supabase.com',
    port: 5432,
    database: 'postgres',
    user: 'postgres.gwlbwekrbwwstjrjpamm',
    password: process.env.PGPASSWORD,
    ssl: {{ rejectUnauthorized: false }}
  }});
  await c.connect();
  const res = await c.query({repr(sql)});
  console.log(JSON.stringify(res.rows, null, 2));
  await c.end();
}})().catch(e => {{ console.error('ERROR:', e.message); process.exit(1); }});
"""
    res = subprocess.run(['node', '-e', node_code], cwd=os.path.dirname(__file__), env=env, text=True, capture_output=True)
    if res.stderr:
        print("STDERR:", res.stderr)
    return res.stdout

if __name__ == '__main__':
    query = sys.argv[1] if len(sys.argv) > 1 else "select count(*) from public.modules"
    print(run_query(query))
