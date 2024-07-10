package progobern.servicios.asignaturasservice.models;

import lombok.*;

import java.util.List;
import java.util.UUID;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class Alumno {
    private UUID id;
    private String nombre;
    private String apellido;
    private String codigo;
    private String correoInstitucional;
    private String correoPersonal;
    private String celular;
    private Boolean egresado;
}
