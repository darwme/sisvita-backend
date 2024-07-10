package progobern.servicios.asignaturasservice.models;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.List;
import java.util.Set;
import java.util.UUID;

@Builder
@Document
@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Asignatura {
    @Id
    private UUID id;
    private Integer codigo;
    private Integer seccion;
    private String nombreDeCurso;
    private String informeFinal;
    private String periodoAcademico;
    private String planEstudios;
    private String programa;
    private String especialidad;
    private Profesor profesor;
    private Tesis tesis;
    private Set<Alumno> alumnos;
    private Integer creditos;
}
