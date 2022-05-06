// server.js

import express from 'express';
import http from 'http';
import { spawn } from 'child_process';

const app = express();
const server = http.createServer(app);

const port = 3000;

app.get('/', (req, res) => {
  let dataToSend;
  const python = spawn('python', ['./src/function_w_args.py', 'jinwook', '30']);
  python.stdout.on('data', (data) => {
    dataToSend = data.toString();
  });

  python.stderr.on('data', (data) => console.log(data.toString()));

  python.on('close', (code) => {
    res.send(dataToSend);
  });
});

server.listen(port, () => {
  console.log(`✅ Listening on http://localhost:${port}`);
});
