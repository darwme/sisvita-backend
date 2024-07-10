package progobern.servicios.asignaturasservice.models;

import lombok.*;

import java.util.UUID;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
public class Profesor {
    private UUID id;
    private String nombre;
    private String codigo;
    private String celular;
    private Boolean investigador;
    private Boolean encargadoEscuela;
    private String correo;
}
