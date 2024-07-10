package progobern.servicios.asignaturasservice.models;

import lombok.*;

import java.time.LocalDate;
import java.util.UUID;
import java.util.List;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class Tesis {
    private UUID id;
    private String codigo;
    private Estado estado;
    private Categoria categoria;
    private List<String> palabrasClave;
    private String urlImagen;
    private String titulo;
    private String resumen;
    private String URI;
    private LocalDate fechaPublicacion;
}
