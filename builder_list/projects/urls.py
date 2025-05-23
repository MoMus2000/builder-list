from django.urls import path
from .views import (
    render_list_projects,
    render_create_project,
    render_checklist,
    save_to_checklist
)

urlpatterns = [
    path(''                                     , render_list_projects),
    path("projects/view/<int:id>"               , render_checklist),
    path("projects/view"                        , render_list_projects),
    path("projects/create"                      , render_create_project),
    path("projects/delete/<int:id>"             , render_create_project),
    path("projects/<int:project_id>/checklist/<int:checklist_id>" , save_to_checklist)
]

