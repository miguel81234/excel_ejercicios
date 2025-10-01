package com.example.sprintmanager.repository;

import com.example.sprintmanager.model.Sprint;
import org.springframework.data.jpa.repository.JpaRepository;

public interface SprintRepository extends JpaRepository<Sprint, Long> {}