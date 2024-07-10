import jwt from "jsonwebtoken";

const checkSession = (req, res, next) => {
  //Bareer
  const headerAuth = req.authorization || req.headers["authorization"];
    if (headerAuth) {
        const token = headerAuth.split(" ").pop();
        jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
            if (err) {
                return res.status(401).send("Token invalido o expirado.");
            }
            req.user = decoded;
            
            //Payload, inicialmente solo info del usuario, tal vez una cookie
            //mas adelante
            req.payload = {
                user: decoded
            };
            
            next();
        });
    } else {
        res.status(401).send("Sin autorización.");
    }
};

export default checkSession;
