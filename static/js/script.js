$(document).ready(function() {
  
    /* Dynamically add new ingredient input field in recipe forms*/
    $(".new-input-btn").on("click", function() {
        $('<input type="text" class="form-control ingredient" name="ingredient" id="ingredient" placeholder="Add ingredient here" required >').insertBefore(".new-input-btn");
    });
    
    /*removes last input element in ingredient list*/
    $(".remove-input-btn").on("click", function() {
        $("#ingredients-details input:last").remove();
    });

       /* Dynamically add new method step input field in recipe forms*/
    $(".new-method-btn").on("click", function() {
        $('<input type="text" class="form-control ingredient" name="method_step" id="method_step" placeholder="Add new step here" required >').insertBefore(".new-method-btn");
    });
    
    /*removes last input element in method step list*/
    $(".remove-method-btn").on("click", function() {
        $("#method_steps-details input:last").remove();
    

    




    });
   
    


   
   
});