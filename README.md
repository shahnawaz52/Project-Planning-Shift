# Project Planning Shift

## Description
The "Project Planning Shift" is an integration solution developed for Odoo that simplifies the management of projects and resource allocation. When a project or task is created within Odoo, this module automatically generates corresponding shifts in the Odoo planning module. This automation bridges the gap between project management and workforce planning, ensuring that resource allocation is directly tied to project needs, which enhances efficiency, reduces manual errors, and streamlines operations across departments.

## Key Features
- **Automatic Shift Creation**: Automatically creates planning shifts in the Odoo planning module whenever a project task is created.
- **Dynamic Resource Allocation**: Allocates shifts based on the project task's assigned users and scheduled times, ensuring optimal resource utilization.
- **Efficient Task Management**: Updates and manages shifts dynamically as project tasks change stages, are reassigned, or updated in terms of scheduling.

## Technical Details
### Models
- `project.task`: Inherits this model to link tasks with planning slots and handle their lifecycle.
- `planning.slot`: Extends to include task shift information and computes allocation percentages and allocated hours based on task assignments.

### Methods
- `_prepare_project_task_shift()`: Prepares or updates planning slots when tasks are created or updated.
- `create()`, `write()`: Overrides these methods to integrate shift planning whenever tasks are created or modified.

### Automated Actions
- **Update Project Task Shift**: An automated server action that triggers the `_prepare_project_task_shift` method to ensure shifts are always synchronized with task updates.

## Installation Instructions
To install the Project Planning Shift module, follow these steps:

1. Ensure you have a working installation of Odoo.
2. Clone this repository to your machine:
git clone https://github.com/yourusername/project-planning-shift.git
3. Add the module to your Odoo addons path:
--addons-path=/path/to/your/addons,/path/to/project-planning-shift
4. Update your Odoo module list and install the module from the Odoo backend interface.

## Usage
After installation, whenever you create a project or task within Odoo, the corresponding shifts will automatically be created in the planning module. To view these shifts, navigate to the Planning module in your Odoo installation.

## Contributing
Contributions to the Project Planning Shift are always welcome. To contribute, please fork the repository, make your changes, and submit a pull request. If you have any questions or require guidance on making contributions, please reach out via the contact information provided below.


