projects = [
    {
        "title": "Portfolio Website",
        "slug": "portfolio-website",
        "brief": "A personal portfolio built with Flask, Bootstrap, and Jinja2.",
        "description": "This project showcases my personal work, skills, and experience. It includes a dynamic project listing, contact form, and animations.",
        "thumbnail": "assets/portfolio.png",
        "tags": ["Flask", "Bootstrap", "Frontend"]
    },
    {
        "title": "Task Manager API",
        "slug": "task-manager-api",
        "brief": "A RESTful API for task management with JWT auth.",
        "description": "Backend system for task tracking with CRUD operations, user authentication, and token-based security using Flask and PostgreSQL.",
        "thumbnail": "assets/api.png",
        "tags": ["Flask", "API", "Backend"]
    },
    {
        "title": "E-Commerce Store",
        "slug": "ecommerce-store",
        "brief": "Full-stack online store with payment integration.",
        "description": "Built with Flask and React, this app includes product listings, user auth, Stripe payments, and an admin dashboard.",
        "thumbnail": "assets/ecommerce.png",
        "tags": ["React", "Flask", "Stripe", "Full-stack"]
    },
    {
        "title": "Blog Platform",
        "slug": "blog-platform",
        "brief": "A multi-user blog site with markdown support and admin controls.",
        "description": "Includes user registration/login, post editing, markdown formatting, and image uploads. Built with Flask, SQLAlchemy, and Bootstrap.",
        "thumbnail": "assets/blog.png",
        "tags": ["Flask", "Markdown", "CMS"]
    }
]

# Optional helper list for tags
tag_list = sorted({tag for project in projects for tag in project['tags']})
