package models

import "gorm.io/gorm"

type Project struct{
  gorm.Model
  ID uint
  Name string `gorm:"not null"`
  Description string
}

