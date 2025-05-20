package main

import (
	"builder-list/models"
	"builder-list/repository"
	"builder-list/routes"
	"fmt"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html/v2"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"

	_ "github.com/mattn/go-sqlite3"
)

func main(){
  db, err := gorm.Open(sqlite.Open("./db/builder-list.db"), &gorm.Config{})

  db.AutoMigrate(
    &models.Project{},
    &models.Checklist{},
    &models.Design{},
    &models.Roof{},
    &models.F1{},
    &models.F2{},
    &models.Basement{},
  )

  if err != nil {
    fmt.Printf("DB not Found in ./db/")
    return
  }

  engine := html.New("./templates", ".html")

  app := fiber.New(fiber.Config{
      Views: engine,
  })

  app.Add(fiber.MethodGet, "/", func (c *fiber.Ctx) error {
    return c.Redirect("/projects")
  })

  project := app.Group("/projects")

  projectRepository   := repository.NewProjectRepository(db)
  checklistRepository := repository.NewChecklistRepository(db)

  pr := routes.NewProjectRouter(*projectRepository)

  project.Add(fiber.MethodGet, "/"           , pr.ViewProjectList)
  project.Add(fiber.MethodGet, "/list"       , pr.ListAllProjects)
  project.Add(fiber.MethodGet, "/view"       , pr.ViewProjectList)
  project.Add(fiber.MethodGet, "/create"     , pr.CreateProjectView)
  project.Add(fiber.MethodPost,"/create"     , pr.CreateProject)
  project.Add(fiber.MethodPost,"/delete/:ID" , pr.DeleteProject)
    
  cl := routes.NewCheckListRoute(checklistRepository)

  project.Add(fiber.MethodGet, "/view/:checklist", cl.ViewCheckList)
  project.Add(fiber.MethodGet, "/checklists", cl.ListAllCheckList)

  app.Listen(":8080")

}

