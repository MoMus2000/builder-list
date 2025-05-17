package repository

import (
	"builder-list/models"

	"gorm.io/gorm"
)

type ProjectRepository struct {
  db *gorm.DB
}

func NewProjectRepository(db *gorm.DB) *ProjectRepository{
  return &ProjectRepository{db}
}

func (pkg *ProjectRepository) FindById(id int) (interface{} , error){
  project := models.Project{}
  pkg.db.First(&project, id)
  return project, nil
}

func (pkg *ProjectRepository) FindAll() (interface{} , error){
  project := []models.Project{}
  pkg.db.Find(&project)
  return project, nil
}

func (pkg *ProjectRepository) Delete(id int) error {
  pkg.db.Delete(&models.Project{}, id)
  return nil
}

func (pkg *ProjectRepository) Create(project *models.Project) error {
  pkg.db.Create(project)
  return nil
}

