const { Client } = require('pg');
const fs = require('fs');
const path = require('path');

const files = process.argv.slice(2);
(async () => {
  const client = new Client({
    host: 'aws-0-ap-southeast-1.pooler.supabase.com',
    port: 5432,
    database: 'postgres',
    user: 'postgres.gwlbwekrbwwstjrjpamm',
    password: process.env.PGPASSWORD,
    ssl: { rejectUnauthorized: false },
  });
  await client.connect();
  for (const f of files) {
    const sql = fs.readFileSync(f, 'utf8');
    process.stdout.write(`Applying ${path.basename(f)} ... `);
    try {
      await client.query(sql);
      console.log('OK');
    } catch (e) {
      console.log('FAILED');
      console.error(e.message, e.position ? `(pos ${e.position})` : '', e.where || '');
      await client.end();
      process.exit(1);
    }
  }
  const r = await client.query(`
    select 
      (select count(*) from public.phases) phases, 
      (select count(*) from public.modules) modules, 
      (select count(*) from public.lessons) lessons, 
      (select count(*) from public.engineering_blogs) blogs, 
      (select count(*) from public.quiz_questions) questions
  `);
  console.log(r.rows[0]);
  await client.end();
})().catch(e => { console.error('ERROR', e.message); process.exit(1); });
