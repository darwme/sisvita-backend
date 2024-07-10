package sisvita.servicios.authservice.tools;

import sisvita.servicios.authservice.models.Alumno;

import java.util.LinkedHashMap;
import java.util.UUID;

public class Convertidor {
    public static Alumno fromLinkedHashMapToAlumno(LinkedHashMap<String,Object> linkedHashMap)
    {
        return Alumno.builder()
                .id(UUID.fromString((String)linkedHashMap.get("alumno_id")))
                .nombre((String) linkedHashMap.get("nombre"))
                .apellido((String) linkedHashMap.get("apellido"))
                .codigo((String) linkedHashMap.get("codigo"))
                .celular((String) linkedHashMap.get("celular"))
                .correoPersonal((String) linkedHashMap.get("correoPersonal"))
                .correoInstitucional((String) linkedHashMap.get("correoInstitucional"))
                .egresado((Integer) linkedHashMap.get("egresado") == 1)
                .build();
    }
    public static LinkedHashMap<String,Object> fromAlumnoToLinkedHashMap(Alumno alumno) throws NoSuchFieldException {
        LinkedHashMap<String,Object> result=new LinkedHashMap<>();
        result.put("alumno_id",alumno.getId());
        result.put("nombre",alumno.getNombre());
        result.put("apellido",alumno.getApellido());
        result.put("codigo",alumno.getCodigo());
        result.put("celular",alumno.getCelular());
        result.put("egresado",alumno.getEgresado());
        result.put("correoPersonal",alumno.getCorreoPersonal());
        result.put("correoInstitucional",alumno.getCorreoInstitucional());
        return result;
    }
}
