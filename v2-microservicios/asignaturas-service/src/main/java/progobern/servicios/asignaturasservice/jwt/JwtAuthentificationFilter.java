package progobern.servicios.asignaturasservice.jwt;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.Arrays;


public class JwtAuthentificationFilter extends OncePerRequestFilter {
    @Override
    protected void doFilterInternal(
            HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        JwtUtil jwtUtil = new JwtUtil();
        try
        {
            String token= request.getHeader("Authorization");
            token=(token!=null)? token.substring(7): token;
            if(token == null || !jwtUtil.validateClaims(token))
            {
                throw new Exception("Invalid token");
            }
        }
        catch (Exception e)
        {
            response.setStatus(HttpStatus.UNAUTHORIZED.value());
            System.out.println(e);
            System.out.println(Arrays.toString(e.getStackTrace()));
            return;
        }
        filterChain.doFilter(request,response);
    }
}
