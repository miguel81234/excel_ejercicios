package com.example.sprintmanager.controller;

import com.example.sprintmanager.model.Sprint;
import com.example.sprintmanager.repository.SprintRepository;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/sprints")
public class SprintController {
    private final SprintRepository sprintRepository;

    public SprintController(SprintRepository sprintRepository) {
        this.sprintRepository = sprintRepository;
    }

    @GetMapping
    public List<Sprint> getAll() {
        return sprintRepository.findAll();
    }

    @PostMapping
    public Sprint create(@RequestBody Sprint sprint) {
        return sprintRepository.save(sprint);
    }
}