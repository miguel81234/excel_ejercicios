package com.example.sprintmanager.repository;

import com.example.sprintmanager.model.TeamMember;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TeamMemberRepository extends JpaRepository<TeamMember, Long> {}