const companyExp = document.querySelectorAll('.exp__company');
const jobExps = document.querySelectorAll('.exp__des');

companyExp.forEach((company, index) => {
    company.addEventListener('click', () => {
        // Remove active class from all companies and hide all job descriptions
        companyExp.forEach((comp, idx) => {
            comp.classList.remove('active--tab');
            jobExps[idx].classList.add('job--none');
            jobExps[idx].classList.remove('active--content');
        });

        // Add active class to the clicked company and show the corresponding job description
        company.classList.add('active--tab');
        jobExps[index].classList.remove('job--none');
        jobExps[index].classList.add('active--content');
    });
});
