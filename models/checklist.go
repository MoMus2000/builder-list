package models

import (
	"gorm.io/gorm"
)

type Checklist struct {
	gorm.Model
  ID        uint `gorm:"primaryKey"`
  Name      string
  ProjectID uint
}

type Design struct {
	gorm.Model
  ID     uint      `gorm:"primaryKey"`
  Todo []string    `gorm:"type:json"`
  ChecklistID uint `gorm:"foreignKey:ChecklistID;"`
}

type Roof struct {
	gorm.Model
  ID     uint `gorm:"primaryKey"`
  Todo []string `gorm:"type:json"`
  ChecklistID uint `gorm:"foreignKey:ChecklistID;"`
}

type F1 struct {
	gorm.Model
  ID     uint `gorm:"primaryKey"`
  Todo []string `gorm:"type:json"`
  ChecklistID uint `gorm:"foreignKey:ChecklistID;"`
}

type F2 struct {
	gorm.Model
  ID     uint `gorm:"primaryKey"`
  Todo []string `gorm:"type:json"`
  ChecklistID uint `gorm:"foreignKey:ChecklistID;"`
}

type Basement struct{
	gorm.Model
  ID     uint `gorm:"primaryKey"`
  Todo []string `gorm:"type:json"`
  ChecklistID uint `gorm:"foreignKey:ChecklistID;"`
}

