def new
    @exercise = Exercise.new
  end
  
  def create
    @exercise = Exercise.new(exercise_params)
  
    if @exercise.save
      redirect_to @exercise
    else
      render :new
    end
  end
  
  private
  
  def exercise_params
    params.require(:exercise).permit(:exercise_name, :weight, :sets, :reps)
  end

  def get_exercise_data
    # Get the exercise name from the URL
    exercise_name = params[:exercise_name]
  
    # Get the weight and sets data from the database
    exercise_data = Exercise.find_by(name: exercise_name)
  
    # Return the data
    return {
      sets: exercise_data.sets,
      weight: exercise_data.weight
    }
  end