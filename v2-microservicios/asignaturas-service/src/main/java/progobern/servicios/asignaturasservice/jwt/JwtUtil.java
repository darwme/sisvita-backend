package progobern.servicios.asignaturasservice.jwt;


import com.auth0.jwt.JWT;
import com.auth0.jwt.interfaces.Claim;
import progobern.servicios.asignaturasservice.models.Asignatura;

import java.nio.charset.StandardCharsets;
import java.util.Date;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class JwtUtil {
    private final String secret = "secret";

    public Map<String, Object> extractClaims(String token)
    {
        return JWT.decode(token).getClaim("data").as((Class<Map<String,Object>>)(Class)Map.class);
    }

    public Date extractExpirationDate(String token){
        return JWT.decode(token).getExpiresAt();
    }

    public boolean validateClaims(String token)
    {
        try {
            return  extractExpirationDate(token).after(new Date());
        } catch (Exception e) {
            throw e;
        }
    }
}
