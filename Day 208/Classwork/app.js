import express from 'express';
import cors from 'cors';

// Server
const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(express.json());