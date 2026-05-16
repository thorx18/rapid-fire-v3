# Step 1 — Install Rails
gem install rails

# Step 2 — Create new Rails app
rails new todo-list

# Step 3 — Go into the folder
cd todo-list

# Step 4 — Generate Task model
rails generate model Task title:string details:text due_date:date completed:boolean

# Step 5 — Generate Tasks controller
rails generate controller Tasks index show new edit

# Step 6 — Run database migration
rails db:migrate

# Step 7 — Start the server
rails server
