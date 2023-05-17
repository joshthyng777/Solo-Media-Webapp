import Vue from 'vue';
import VueCharts from 'vue-chartjs';

Vue.use(VueCharts);

new Vue({
  el: '#app',
  data() {
    return {
      exercises: [],
      chartData: {
        labels: [],
        datasets: [{
          data: [],
          label: 'Weight'
        }]
      }
    };
  },
  mounted() {
    this.getExercises();
  },
  methods: {
    getExercises() {
      fetch('/exercises')
        .then(response => response.json())
        .then(data => {
          this.exercises = data;
          this.chartData.labels = data.map(exercise => exercise.sets);
          this.chartData.datasets[0].data = data.map(exercise => exercise.weight);
        });
    }
  }
});

chartData = {
    labels: [],
    datasets: [{
      data: [],
      label: 'Weight'
    }]
    };
    
    // Get the exercise name from the URL
    var exerciseName = window.location.search.substring(1).split("&")[0].split("=")[1];
    
    // Get the weight and sets data from the database
    $.ajax({
    url: "/get-exercise-data",
    data: {
      exercise_name: exerciseName
    },
    success: function(data) {
      chartData.labels = data.sets;
      chartData.datasets[0].data = data.weight;
    }
    });
    
    // Create the graph
    var chart = new Chart(document.getElementById("chart"), {
    type: "line",
    data: chartData,
    options: {
      title: exerciseName
    }
    });