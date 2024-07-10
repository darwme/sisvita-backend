package sisvita.servicios.authservice.controllers;

import jdk.jfr.ContentType;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.*;
import sisvita.servicios.authservice.models.Alumno;

import java.awt.*;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@FeignClient(name = "usuarios-service")
public interface UsuarioController {
    @PostMapping("auth/login")
    public LinkedHashMap<String,Object> login(@RequestBody Map<String,Object> request);
    @GetMapping("alumnos/{codigo}")
    public List<LinkedHashMap<String,Object>> getByCodigo(
            @PathVariable String codigo);

    @PostMapping("alumnos")
    public List<LinkedHashMap<String,Object>> getAlumnos();

    @PostMapping("auth/register")
    public void setUsuario(@RequestBody LinkedHashMap<String,Object> usuario);

    @DeleteMapping("alumnos/{codigo}")
    public String deleteAlumnoByCodigo(@PathVariable String codigo);

    @GetMapping("auth/usuario/{id}")
    public List<LinkedHashMap<String,Object>> getUsuarioById(@PathVariable String id);
}