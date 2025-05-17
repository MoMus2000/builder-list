package routes

import (
	"builder-list/models"
	"builder-list/repository"
	"strconv"

	"github.com/gofiber/fiber/v2"
)

type ProjectRouter struct {
  pr *repository.ProjectRepository
}

func NewProjectRouter(pr repository.ProjectRepository) ProjectRouter{
  return ProjectRouter{&pr}
}

func (pr *ProjectRouter) CreateProjectView(c *fiber.Ctx) error{
  return c.Render(
    "create-project", nil,
  )
}

func (pr *ProjectRouter) CreateProject(c *fiber.Ctx) error{
  pr.pr.Create(&models.Project{
    Name:        c.FormValue("name"),
    Description: c.FormValue("description"),
  })
  return c.Redirect("/projects")
}

func (pr *ProjectRouter) DeleteProject(c *fiber.Ctx) error {
  deleteID, _ := strconv.Atoi(c.Params("ID"))
  pr.pr.Delete(deleteID)
  return c.Redirect("/projects")
}

func (pr *ProjectRouter) ViewProjectList(c *fiber.Ctx) error{
  projects, _ := pr.pr.FindAll()
  return c.Render(
    "list-projects", fiber.Map{
      "Title": "Current Projects",
      "Projects": projects,
    },
  )
}

func (pr *ProjectRouter) ListAllProjects(c *fiber.Ctx) error {
  projects, _ := pr.pr.FindAll()

  return c.JSON(
    fiber.Map{
      "projects": projects,
    },
  )
}

