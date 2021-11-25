from stacks.models import Project, Programming_language, Service, Library, Framework
import pytest


@pytest.fixture
def twada():
    return Project(name='Twada', url_name=('twada'))


@pytest.fixture
def python():
    return Programming_language(name='python', url_name='python')


@pytest.fixture
def github():
    return Service(name='github', url_name='github')


@pytest.fixture
def library():
    return Library(name='library', url_name='library')


@pytest.fixture
def framework():
    return Framework(name='framework', url_name='framework')


class Test_twada_chooses_python:
    @pytest.fixture(autouse=True)
    def twada_chooses_python(self, twada, python):
        twada.programming_languages.append(python)

    @pytest.fixture
    def choice(self, twada):
        return twada.choices[0]

    class Test_twada:
        def test_choices_has_one_value(self, twada):
            assert len(twada.choices) == 1

        def test_programming_languages_also_has_one(self, twada):
            assert len(twada.programming_languages) == 1

        def test_tawada_also_has_the_same_programming_languages(self, twada, python):
            assert twada.programming_languages[0] is python

    class Test_python:
        def test_choices_has_one_value(self, python):
            assert len(python.choices) == 1

        def test_choice_same_as_twada_choice(self, choice, python):
            assert python.choices[0] is choice

        def test_projects_has_one_value(self, python):
            assert len(python.projects) == 1

        def test_projects_is_twada(self, python, twada):
            assert python.projects[0] is twada

    class Test_twada_choice:
        def test_project_is_twada(self, choice, twada):
            assert choice.project is twada

        def test_programming_language_is_python(self, choice, python):
            assert choice.programming_language is python


class Test_twada_chooses_github:
    @pytest.fixture(autouse=True)
    def twada_chooses_github(self, twada, github):
        twada.services.append(github)

    @pytest.fixture
    def choice(self, twada):
        return twada.service_choice[0]

    class Test_twada:
        def test_choices_has_one_value(self, twada):
            assert len(twada.service_choice) == 1

        def test_service_also_has_one(self, twada):
            assert len(twada.services) == 1

        def test_tawada_also_has_the_same_service(self, twada, github):
            assert twada.services[0] is github

    class Test_github:
        def test_service_choices_has_one_value(self, github):
            assert len(github.service_choice) == 1

        def test_choice_same_as_twada_choice(self, choice, github):
            assert github.service_choice[0] is choice

        def test_projects_has_one_value(self, github):
            assert len(github.projects) == 1

        def test_projects_is_twada(self, github, twada):
            assert github.projects[0] is twada

    class Test_twada_service_choice:
        def test_project_is_twada(self, choice, twada):
            assert choice.project is twada

        def test_service_is_github(self, choice, github):
            assert choice.service is github


class Test_twada_chooses_library:
    @pytest.fixture(autouse=True)
    def twada_chooses_library(self, twada, library):
        twada.libraries.append(library)

    @pytest.fixture
    def choice(self, twada):
        return twada.library_choice[0]

    class Test_twada:
        def test_choices_has_one_value(self, twada):
            assert len(twada.library_choice) == 1

        def test_library_also_has_one(self, twada):
            assert len(twada.libraries) == 1

        def test_twada_also_has_the_same_library(self, twada, library):
            assert twada.libraries[0] is library

    class Test_library:
        def test_library_choices_has_one_value(self, library):
            assert len(library.library_choice) == 1

        def test_choice_same_as_twada_choice(self, choice, library):
            assert library.library_choice[0] is choice

        def test_library_has_one_value(self, library):
            assert len(library.projects) == 1

        def test_projects_is_twada(self, library, twada):
            assert library.projects[0] is twada

    class Test_twada_library_choice:
        def test_library_is_twada(self, choice, twada):
            assert choice.project is twada

        def test_library_is_library(self, choice, library):
            assert choice.library is library


class Test_twada_chooses_framework:
    @pytest.fixture(autouse=True)
    def twada_chooses_framework(self, twada, framework):
        twada.frameworks.append(framework)

    @pytest.fixture
    def choice(self, twada):
        return twada.framework_choice[0]

    class Test_twada:
        def test_choices_has_one_value(self, twada):
            assert len(twada.framework_choice) == 1

        def test_framework_also_has_one(self, twada):
            assert len(twada.frameworks) == 1

        def test_twada_also_has_the_same_framework(self, twada, framework):
            assert twada.frameworks[0] is framework

    class Test_framework:
        def test_framework_choices_has_one_value(self, framework):
            assert len(framework.framework_choice) == 1

        def test_choice_same_as_twada_choice(self, choice, framework):
            assert framework.framework_choice[0] is choice

        def test_framework_has_one_value(self, framework):
            assert len(framework.projects) == 1

        def test_projects_is_twada(self, framework, twada):
            assert framework.projects[0] is twada

    class Test_twada_framework_choice:
        def test_library_is_twada(self, choice, twada):
            assert choice.project is twada

        def test_library_is_framework(self, choice, framework):
            assert choice.framework is framework
