package com.example.sprintmanager.model;

import jakarta.persistence.*;

@Entity
public class UserStory {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descripcion;
    private int estimacion;

    @ManyToOne
    @JoinColumn(name="sprint_id")
    private Sprint sprint;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }

    public int getEstimacion() { return estimacion; }
    public void setEstimacion(int estimacion) { this.estimacion = estimacion; }

    public Sprint getSprint() { return sprint; }
    public void setSprint(Sprint sprint) { this.sprint = sprint; }
}