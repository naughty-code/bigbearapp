$(document).ready(function() {
	function search() {
		var alertError = $('.alert-danger')
		var progressBar = $('.progress')
		progressBar.removeClass('d-none')
		alertError.addClass('d-none')
		$.get('https://bigbearcabinsapp-api-heroku.herokuapp.com/api')
			.done(function( data ) {
				progressBar.addClass('d-none')
				$('#example').DataTable( {
					data: data,
					columns: [
						{ title: "IDVRM" },
						{ title: "ID" },
						{ title: "NAME" },
						{ title: "WEBSITE" },
						{
							title: "DESCRIPTION",
							render: function ( data, type, row ) {
								return `<span class="d-inline-block text-truncate" data-toggle="tooltip" style="max-width: 150px;" title="${data}">
								${data}
							  </span>`;
							}
						},
						{ title: "ADRESS" },
						{ title: "LOCATION" },
						{ title: "BEDROOMS" },
						{ title: "OCCUPANCY" },
						{ title: "TIER" },
						{ title: "STATUS" }
					]
				} );
				$('[data-toggle="tooltip"]').tooltip();
			})
			.fail(function() {
				progressBar.addClass('d-none')
				alertError.removeClass('d-none')
			})
	}
	search();
	let dataSet = [
		['idvrm', 'id', 'name',	'website', 'descriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescriptiondescription', 'address', 'location', 'bedrooms', 'occupancy', 'tier', 'status'],
		['idvrm', 'id', 'name',	'website', 'description', 'address', 'location', 'bedrooms', 'occupancy', 'tier', 'status'],
		['idvrm', 'id', 'name',	'website', 'description', 'address', 'location', 'bedrooms', 'occupancy', 'tier', 'status'],
		['idvrm', 'id', 'name',	'website', 'description', 'address', 'location', 'bedrooms', 'occupancy', 'tier', 'status']
	]
} );
