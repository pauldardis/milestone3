$(document).ready(function() {
  
    /* Dynamically add new ingredient input field in recipe forms*/
    $(".new-input-btn").on("click", function() {
        $('<input type="text" class="form-control ingredient" name="ingredient" id="ingredient" placeholder="Add ingredient here" required >').insertBefore(".new-input-btn");
    });
    
    /*removes last input element in ingredient list*/
    $(".remove-input-btn").on("click", function() {
        $("#ingredients-details input:last").remove();
    });
   
   
});