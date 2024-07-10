package progobern.servicios.asignaturasservice.controllers;


import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import progobern.servicios.asignaturasservice.jwt.JwtUtil;
import progobern.servicios.asignaturasservice.models.Asignatura;
import progobern.servicios.asignaturasservice.models.Profesor;
import progobern.servicios.asignaturasservice.models.Tesis;
import progobern.servicios.asignaturasservice.services.AsignaturaService;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor

public class AsignaturaController {
    private final AsignaturaService service;

    // ROLES: ADMIN
    @PostMapping(path="asignatura")
    public ResponseEntity<String> createAsignatura(@RequestHeader String Authorization,@RequestBody Asignatura request)
    {
        return service.createAsignatura(Authorization,request);
    }
    // TODOS
    @GetMapping(path = "asignaturas")
    public ResponseEntity<List<Asignatura>> getAsignaturas(@RequestHeader String Authorization)
    {
        return service.getAsignaturas();
    }
    // TODOS
    @PostMapping(path = "asignatura-tesis")
    public ResponseEntity<List<Asignatura>> getAsignaturaByTesis(@RequestHeader String Authorization,
                                                                 @RequestBody Tesis request)
    {
        return service.findByTesis(request);
    }
    //TODOS
    @PostMapping(path = "asignatura-profesor")
    public ResponseEntity<List<Asignatura>> getAsignaturaByProfesor(@RequestHeader String Authorization,
                                                                    @RequestBody Profesor request)
    {
        return service.findByProfesor(request);
    }
    //TODOS
    @GetMapping(path = "asignatura-codigo-seccion/{codigo}/{seccion}")
    public ResponseEntity<Asignatura> getAsignaturaByCodigoAndSeccion(
            @RequestHeader String Authorization,
            @PathVariable String codigo,
            @PathVariable String seccion)
    {
        return service.findByCodigoAndSeccion(Integer.parseInt(codigo),Integer.parseInt(seccion));
    }
    //ADMIN
    @DeleteMapping(path = "asignatura/{id}")
    public ResponseEntity<String> deleteAsignatura(@PathVariable String id,
                                                   @RequestHeader String Authorization)
    {
        return service.deleteById(Authorization,id);
    }
    //PROFESORES

    @GetMapping(path= "asignatura-reservarAlumno/{codigo}/{seccion}/{alumnoCodigo}")
    public ResponseEntity<String> reservarAlumno(@PathVariable Integer codigo,
                                                 @PathVariable Integer seccion,
                                                 @PathVariable String alumnoCodigo,
                                                 @RequestHeader String Authorization)
    {
        return service.reservarAlumno(Authorization,codigo,seccion,alumnoCodigo);
    }
    // PROFESORES
    @GetMapping(path = "asignatura-esAlumnoReservado/{codigo}/{seccion}/{alumnoCodigo}")
    public ResponseEntity<Boolean> esAlumnoReservado(@PathVariable Integer codigo,
                                                     @PathVariable Integer seccion,
                                                     @PathVariable String alumnoCodigo,
                                                     @RequestHeader String Authorization)
    {
        return service.alumnoEstaReservado(Authorization,codigo,seccion,alumnoCodigo);
    }
    //TODOS
    @GetMapping(path = "asignatura-creditosPorCiclo/{alumnoCodigo}")
    public ResponseEntity<Map<String,Integer>> getCreditosByCiclo(@PathVariable String alumnoCodigo,
                                                                  @RequestHeader String Authorization)
    {
        return service.getCreditosByCiclo(alumnoCodigo);
    }
    //TODOS
    @GetMapping(path="asignatura/{id}")
    public ResponseEntity<Asignatura> findByAsignaturaById(@PathVariable String id,
                                                           @RequestHeader String Authorization)
    {
        return service.findById(id);
    }
    //TESTING (CUENTA ESPECIAL)
    @DeleteMapping(path = "asignatura/truncarDatos")
    public ResponseEntity<String> deleteAll(@RequestHeader String Authorization)
    {
        return service.deleteAll();
    }
}
