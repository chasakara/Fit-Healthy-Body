from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Reviews
from .forms import ReviewsForm


def allreviews(request):
    reviews = Reviews.objects.all()

    return render(request, 'reviews/all_reviews.html', {'reviews': reviews})


def review_detail(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)

    return render(request, 'reviews/review_detail.html', {'review': review})


def add_review(request):
    """ Add a review """
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('review_detail', args=[review.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')


    form = ReviewsForm()

    template = 'review/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

