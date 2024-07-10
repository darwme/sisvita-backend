package sisvita.servicios.authservice.controllers;


import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import sisvita.servicios.authservice.jwt.JwtUtil;
import sisvita.servicios.authservice.models.Asignatura;
import sisvita.servicios.authservice.models.Profesor;
import sisvita.servicios.authservice.models.Tesis;
import sisvita.servicios.authservice.services.AuthService;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor

public class AsignaturaController {
    private final AuthService service;

    // ROLES: ADMIN
    @PostMapping(path="asignatura")
    public ResponseEntity<String> createAsignatura(@RequestBody Asignatura request)
    {
        return service.createAsignatura(request);
    }
    // TODOS
    @GetMapping(path = "asignaturas")
    public ResponseEntity<List<Asignatura>> getAsignaturas()
    {
        return service.getAsignaturas();
    }
    // TODOS
    @PostMapping(path = "asignatura-tesis")
    public ResponseEntity<List<Asignatura>> getAsignaturaByTesis(@RequestBody Tesis request)
    {
        return service.findByTesis(request);
    }
    //TODOS
    @PostMapping(path = "asignatura-profesor")
    public ResponseEntity<List<Asignatura>> getAsignaturaByProfesor(@RequestBody Profesor request)
    {
        return service.findByProfesor(request);
    }
    //TODOS
    @GetMapping(path = "asignatura-codigo-seccion/{codigo}/{seccion}")
    public ResponseEntity<Asignatura> getAsignaturaByCodigoAndSeccion(
            @PathVariable String codigo,
            @PathVariable String seccion)
    {
        return service.findByCodigoAndSeccion(Integer.parseInt(codigo),Integer.parseInt(seccion));
    }
    //ADMIN
    @DeleteMapping(path = "asignatura/{id}")
    public ResponseEntity<String> deleteAsignatura(@PathVariable String id)
    {
        return service.deleteById(id);
    }
    //PROFESORES

    @GetMapping(path= "asignatura-reservarAlumno/{codigo}/{seccion}/{alumnoCodigo}")
    public ResponseEntity<String> reservarAlumno(@PathVariable Integer codigo,
                                                 @PathVariable Integer seccion,
                                                 @PathVariable String alumnoCodigo)
    {
        return service.reservarAlumno(codigo,seccion,alumnoCodigo);
    }
    // PROFESORES
    @GetMapping(path = "asignatura-esAlumnoReservado/{codigo}/{seccion}/{alumnoCodigo}")
    public ResponseEntity<Boolean> esAlumnoReservado(@PathVariable Integer codigo,
                                                     @PathVariable Integer seccion,
                                                     @PathVariable String alumnoCodigo)
    {
        return service.alumnoEstaReservado(codigo,seccion,alumnoCodigo);
    }
    //TODOS
    @GetMapping(path = "asignatura-creditosPorCiclo/{alumnoCodigo}")
    public ResponseEntity<Map<String,Integer>> getCreditosByCiclo(@PathVariable String alumnoCodigo)
    {
        return service.getCreditosByCiclo(alumnoCodigo);
    }
    //TODOS
    @GetMapping(path="asignatura/{id}")
    public ResponseEntity<Asignatura> findByAsignaturaById(@PathVariable String id)
    {
        return service.findById(id);
    }
    //TESTING (CUENTA ESPECIAL)
    @DeleteMapping(path = "asignatura/truncarDatos")
    public ResponseEntity<String> deleteAll()
    {
        return service.deleteAll();
    }
}
