@app.route('/get_recipes?limit=6&offset=0')
def get_recipes():
    # page_size = 10
    # current_page = int(request.args.get('current_page', 1))
    # total = mongo.db.recipes.count()
    # pages = range(1, int(math.ceil(total / page_size)) + 1)
    # recipes = mongo.db.recipes.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1) * page_size).limit(page_size)
    # return render_template("showall.html", recipes=recipes, current_page=current_page, pages=pages)
    
    <div class="container">
    {% if args.num_results > args.p_limit %}
    <div class="row">
        <div class="col-sm-12 card text-center">
            <img src="{{recipe.photo_url}}" class="card-img-top" alt="...">
            <div class="card-body text-center">
                <h5 class="card-title">{{recipes.recipe_name}}</h5>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item"><i class="fas fa-utensils"></i> Servings: {{recipe.servings}}</li>
                    <li class="list-group-item"><i class="far fa-clock"></i> Preptime: {{recipe.preptime}}</li>
                    <li class="list-group-item">{{recipe.tags}}</li>
                </ul>
                <a href="#" class="btn btn-primary">View Full Recipe</a>
            </div>
        </div>
    </div>
    
    <div class="row">
        
        <nav aria-label="Page navigation example">
            <ul class="pagination text-center">
                
                <li class="page-item disabled">
                    {% if args.p_offset > 0 %}
                    <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                    {% endif %}
                </li>
                <li class="page-item active"><a class="page-link" href="{{ url_for('get_recipes' }}">{{page_number}}</a></li>

                <li class="page-item"><a class="page-link" href="{{ url_for('get_recipes', current_page=page_number) }}">{{page_number}}</a></li>
                <!--<li class="page-item"><a class="page-link" href="#">2</a></li>-->
                <!--<li class="page-item"><a class="page-link" href="#">3</a></li>-->

                <li class="page-item">
                    {% if args.p_offset + args.p_limit < args.num_results  %}
                    <a class="page-link" href="#">Next</a>
                    {% endif %}
                </li>
                
            </ul>
        </nav>
    </div>
    
</div>
{% endif %}


<img src="{{recipes.photo_url}}" class="card-img-top" alt="...">-->