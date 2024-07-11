package sm.dsw.sisvita.auth.model;

import jakarta.persistence.*;
import lombok.*;
import java.util.Date;

@Entity
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "ubicacion")

public class Ubicacion {
    @Id
    private Long ubigeo;

    @Column(name = "provincia")
    private String provincia;

    @Column(name = "distrito")
    private String distrito;

    @Column(name = "x")
    private double x;
    
    @Column(name = "y")
    private double y;
}
