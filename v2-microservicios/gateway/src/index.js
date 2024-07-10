import express, {response} from "express";
import morgan from "morgan";
import { createProxyMiddleware , fixRequestBody} from "http-proxy-middleware";
import dotenv from "dotenv";
import {findRoutes} from "./eureka-helper.js";

const app = express();
let [ USERS_API_URL, AUTH_API_URL ,IDEA_TESIS_API_URL] = ["","",""];
dotenv.config();
findRoutes().then(routes=>{
  AUTH_API_URL=routes.find((route) => route.name==="AUTH-SERVICE").url;
  app.use(express.json());
  app.use(morgan("combined"));
  app.get("/", (req, res) => {
    res.status(200).json({
      message: routes
    });
  });

  const optionsAuth = {
    target: AUTH_API_URL,
    changeOrigin: true,
    pathRewrite: {
      [`^/a`]: AUTH_API_URL,
    },
    logger: console,
    onProxyReq: fixRequestBody,
  };

  app.use("/a", createProxyMiddleware(optionsAuth));

  const port = process.env.PORT || 3000;

  app.listen(port, () => {
    console.log(`Gateway Server is running on port ${port}`);
  });
}).catch((error) => console.log(error));

