var Citizen = function(name, country){
  this.name = name;
  this.country = country;
};

Citizen.prototype = {
  printDetails: function(){
    console.log('Citizen' + this.name + ' from ' + this.country);
  }
};

var c = new Citizen('Groucho M.', 'Fredonia');

c.printDetails();

typeof(c)
