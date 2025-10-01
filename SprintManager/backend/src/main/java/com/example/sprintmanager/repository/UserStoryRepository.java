package com.example.sprintmanager.repository;

import com.example.sprintmanager.model.UserStory;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserStoryRepository extends JpaRepository<UserStory, Long> {}