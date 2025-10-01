package com.example.sprintmanager.controller;

import com.example.sprintmanager.model.UserStory;
import com.example.sprintmanager.repository.UserStoryRepository;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/userstories")
public class UserStoryController {
    private final UserStoryRepository userStoryRepository;

    public UserStoryController(UserStoryRepository userStoryRepository) {
        this.userStoryRepository = userStoryRepository;
    }

    @GetMapping
    public List<UserStory> getAll() {
        return userStoryRepository.findAll();
    }

    @PostMapping
    public UserStory create(@RequestBody UserStory userStory) {
        return userStoryRepository.save(userStory);
    }
}