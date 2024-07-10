import express, {response} from "express";
import morgan from "morgan";
import { createProxyMiddleware , fixRequestBody} from "http-proxy-middleware";
import dotenv from "dotenv";
import {findRoutes} from "./eureka-helper.js";

const app = express();
let [ USERS_API_URL, ASIGNATURAS_API_URL ,IDEA_TESIS_API_URL] = ["",""];
dotenv.config();
findRoutes().then(routes=>{
  USERS_API_URL=routes.find(route => route.name==="USUARIOS-SERVICE").url;
  ASIGNATURAS_API_URL=routes.find(route => route.name==="ASIGNATURA-SERVICE").url;
  IDEA_TESIS_API_URL=routes.find(route => route.name==="IDEA-TESIS-SERVICE").url;
  app.use(express.json());
  app.use(morgan("combined"));
  app.get("/", (req, res) => {
    res.status(200).json({
      message: routes
    });
  });
  const optionsUsers = {
    target: USERS_API_URL,
    changeOrigin: true,
    pathRewrite: {
      [`^/u/api`]: USERS_API_URL,
    },
    logger: console,
    onProxyReq: fixRequestBody,
  };

  const optionsAsignaturas = {
    target: ASIGNATURAS_API_URL,
    changeOrigin: true,
    pathRewrite: {
      [`^/a`]: ASIGNATURAS_API_URL,
    },
    logger: console,
    onProxyReq: fixRequestBody,
  };
  const optionsIdeas_Tesis = {
    target: IDEA_TESIS_API_URL,
    changeOrigin: true,
    pathRewrite: {
      [`^/it/api`]: IDEA_TESIS_API_URL,
    },
    logger: console,
    onProxyReq: fixRequestBody,
  };

  app.use("/u/api", createProxyMiddleware(optionsUsers));
  app.use("/a", createProxyMiddleware(optionsAsignaturas));
  app.use("/it/api", createProxyMiddleware(optionsIdeas_Tesis));

  const port = process.env.PORT || 3000;

  app.listen(port, () => {
    console.log(`Gateway Server is running on port ${port}`);
  });
}).catch((error) => console.log(error));

