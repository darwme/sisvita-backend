package progobern.servicios.asignaturasservice.services;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.coyote.Response;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.ExampleMatcher;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import progobern.servicios.asignaturasservice.controllers.UsuarioController;
import progobern.servicios.asignaturasservice.jwt.JwtUtil;
import progobern.servicios.asignaturasservice.models.Alumno;
import progobern.servicios.asignaturasservice.models.Asignatura;
import progobern.servicios.asignaturasservice.models.Profesor;
import progobern.servicios.asignaturasservice.models.Tesis;
import progobern.servicios.asignaturasservice.repositories.AsignaturaRepository;
import progobern.servicios.asignaturasservice.tools.Convertidor;

import java.util.*;

@Service
@Slf4j
@RequiredArgsConstructor
public class AsignaturaService {
    private final AsignaturaRepository repository;
    private final UsuarioController usuarioController;
    private final JwtUtil jwtUtil = new JwtUtil();
    public ResponseEntity<String> createAsignatura(String Authorization,Asignatura request){
        Map<String,Object> claims=jwtUtil.extractClaims(Authorization.substring(7));
        if(claims.get("administrador").equals(1))
        {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Se necesita permisos de administrador");
        }
        ExampleMatcher exampleMatcher=ExampleMatcher.matching()
                .withIgnorePaths("id")
                .withIncludeNullValues();
        boolean sameAsignatura=!repository.findAll(Example.of(request,exampleMatcher)).isEmpty();
        if(!sameAsignatura)
        {
            repository.save(request);
        }
        return sameAsignatura ? ResponseEntity.badRequest().body("Asignatura ya existente")
                : ResponseEntity.ok("Asignatura creada satisfactoriamente");
    }
    public ResponseEntity<List<Asignatura>> getAsignaturas()
    {
        return ResponseEntity.ok(repository.findAll());
    }
    public ResponseEntity<List<Asignatura>> findByTesis(Tesis request)
    {
        return ResponseEntity.ok(repository.findByTesis(request));
    }
    public ResponseEntity<List<Asignatura>> findByProfesor(Profesor request)
    {
        return ResponseEntity.ok(repository.findByProfesor(request));
    }
    public ResponseEntity<Asignatura> findByCodigoAndSeccion(Integer codigo,Integer seccion)
    {
        return ResponseEntity.ok(repository.findByCodigoAndSeccion(codigo,seccion));
    }
    public ResponseEntity<String> deleteById(String Authorization,String id)
    {
        Map<String,Object> claims=jwtUtil.extractClaims(Authorization.substring(7));
        if(claims.get("administrador").equals(1))
        {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Se necesita permisos de administrador");
        }
        ResponseEntity<String> result ;
        if(repository.findAll().stream()
                .noneMatch(asignatura -> asignatura.getId().toString().equals(id)))
        {
            result = new ResponseEntity<>("Asignatura no existente",HttpStatusCode.valueOf(404));
        }
        else {
            result = new ResponseEntity<>("Asignatura borrada exitosamente",HttpStatusCode.valueOf(200));
        }
        return result;
    }

    public ResponseEntity<Asignatura> findById(String id)
    {
        return ResponseEntity.of(repository.findById(UUID.fromString(id)));
    }
    public ResponseEntity<String> reservarAlumno(String Authorization,Integer codigo, Integer seccion,String alumnoCodigo)
    {
        Map<String,Object> claims=jwtUtil.extractClaims(Authorization.substring(7));
        if(claims.get("administrador").equals(1))
        {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Se necesita permisos de administrador");
        }
        Asignatura asignatura=repository.findByCodigoAndSeccion(codigo,seccion);
        //System.out.println(usuarioController.getByCodigo(alumnoCodigo));
        Alumno alumno= Convertidor.fromLinkedHashMapToAlumno(usuarioController.getByCodigo(Authorization,alumnoCodigo).get(0));
        ResponseEntity<String> result;
        if(repository.exists(Example.of(asignatura)))
        {
            asignatura.getAlumnos().add(alumno);
            repository.save(asignatura);
            result= ResponseEntity.ok("Alumno agregado a la lista");
        }
        else {
            result= ResponseEntity.badRequest().body(alumno.toString());
        }
        return result;
    }
    public ResponseEntity<Boolean> alumnoEstaReservado(String Authorization,Integer codigo, Integer seccion,String alumnoCodigo)
    {
        Map<String,Object> claims=jwtUtil.extractClaims(Authorization.substring(7));
        String rol = (String) claims.get("rol");
        if(rol.equalsIgnoreCase("profesor"))
        {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(false);
        }
        Asignatura asignatura=repository.findByCodigoAndSeccion(codigo,seccion);
        return ResponseEntity.of(Optional.of(asignatura.getAlumnos().stream().anyMatch(alumno -> alumno.getCodigo().equals(alumnoCodigo))));
    }

    public ResponseEntity<Map<String,Integer>> getCreditosByCiclo(String alumnoCodigo)
    {
        List<Asignatura> asignaturas= repository.findAll();
        List<String> periodosAcademicos= asignaturas.stream().filter(asignatura ->
                        asignatura.getAlumnos()
                                .stream()
                                .anyMatch(alumno1 -> alumno1.getCodigo().equals(alumnoCodigo)))
                .map(Asignatura::getPeriodoAcademico)
                .toList();
        Map<String,Integer> result=new HashMap<>();
        System.out.println(periodosAcademicos);
        for(String periodosAcademico:periodosAcademicos)
        {
            int conteo=asignaturas.stream()
                    .filter(asignatura -> asignatura.getPeriodoAcademico().equals(periodosAcademico)
            && asignatura.getAlumnos().stream().anyMatch(alumno -> alumno.getCodigo().equals(alumnoCodigo)))
                    .mapToInt(Asignatura::getCreditos).sum();
            result.put(periodosAcademico,conteo);
        }
        System.out.println(result);
        return ResponseEntity.ok(result);
    }
    public ResponseEntity<String> deleteAll(){
        repository.deleteAll();
        return ResponseEntity.of(Optional.of("Datos truncados"));
    }
}