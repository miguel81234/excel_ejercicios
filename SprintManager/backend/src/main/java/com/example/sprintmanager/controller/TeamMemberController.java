package com.example.sprintmanager.controller;

import com.example.sprintmanager.model.TeamMember;
import com.example.sprintmanager.repository.TeamMemberRepository;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/team")
public class TeamMemberController {
    private final TeamMemberRepository teamMemberRepository;

    public TeamMemberController(TeamMemberRepository teamMemberRepository) {
        this.teamMemberRepository = teamMemberRepository;
    }

    @GetMapping
    public List<TeamMember> getAll() {
        return teamMemberRepository.findAll();
    }

    @PostMapping
    public TeamMember create(@RequestBody TeamMember teamMember) {
        return teamMemberRepository.save(teamMember);
    }
}