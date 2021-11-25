from datetime import timezone
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.sql import func

Base = declarative_base()


class Programming_language(Base):
    __tablename__ = 'programming_languages'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url_name = Column(String(255), nullable=False, unique=True, index=True)
    choices = relationship('Programming_language_choice',
                           back_populates='programming_language')
    projects = association_proxy(
        'choices', 'project', creator=lambda pj: Programming_language_choice(project=pj))

    def __repr__(self):
        return "<Programming languages (id='%s', url='%s'>" % (self.id, self.url_name)


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url_name = Column(String(255), nullable=False, index=True, unique=True)
    choices = relationship('Programming_language_choice',
                           back_populates='project')
    programming_languages = association_proxy(
        'choices', 'programming_language', creator=lambda pl: Programming_language_choice(programming_language=pl))
    service_choice = relationship('Service_choice', back_populates='project')
    services = association_proxy(
        'service_choice', 'service', creator=lambda sv: Service_choice(service=sv))
    library_choice = relationship('Library_choice', back_populates='project')
    libraries = association_proxy(
        'library_choice', 'library', creator=lambda lb: Library_choice(library=lb))
    framework_choice = relationship(
        'Framework_choice', back_populates='project')
    frameworks = association_proxy(
        'framework_choice', 'framework', creator=lambda fw: Framework_choice(framework=fw))

    def __repr__(self):
        return "<Project (id='%s', name='%s', url='%s')>" % (self.id, self.name, self.url_name)


class Programming_language_choice(Base):
    __tablename__ = 'programming_language_choices'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    Programming_language_id = Column(Integer, ForeignKey(
        'programming_languages.id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    project = relationship('Project', back_populates='choices')
    programming_language = relationship(
        'Programming_language', back_populates='choices')

    def __repr__(self):
        return "<Choice (id='%s', project id='%s', programming language id='%s')>" % (self.id, self.project_id, self.Programming_language_id)


class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url_name = Column(String(255), nullable=False)
    service_choice = relationship('Service_choice', back_populates='service')
    projects = association_proxy(
        'service_choice', 'project', creator=lambda pj: Service_choice(project=pj))

    def __repr__(self):
        return "<Service (id='%s', name='%s', url='%s')>" % (self.id, self.name, self.url_name)


class Service_choice(Base):
    __tablename__ = 'service_choices'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    project = relationship('Project', back_populates='service_choice')
    service = relationship('Service', back_populates='service_choice')

    def __repr__(self):
        return "<Service choice (id='%s', project id ='%s', service_id = '%s')>" % (self.id, self.project_id, self.service_id)


class Library(Base):
    __tablename__ = 'libraries'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url_name = Column(String(255), nullable=False)
    library_choice = relationship('Library_choice', back_populates='library')
    projects = association_proxy(
        'library_choice', 'project', creator=lambda pj: Library_choice(project=pj))

    def __repr__(self):
        return "<Library (id='%s', name='%s', url='%s')>" % (self.id, self.name, self.url_name)


class Library_choice(Base):
    __tablename__ = 'library_choices'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    library_id = Column(Integer, ForeignKey('libraries.id'), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    project = relationship('Project', back_populates='library_choice')
    library = relationship('Library', back_populates='library_choice')

    def __repr__(self):
        return "<Library choice (id='%s', project id ='%s', library_id = '%s')>" % (self.id, self.project_id, self.library_id)


class Framework(Base):
    __tablename__ = 'frameworks'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    url_name = Column(String(255), nullable=False)
    framework_choice = relationship(
        'Framework_choice', back_populates='framework')
    projects = association_proxy(
        'framework_choice', 'project', creator=lambda fw: Framework_choice(framework=fw))

    def __repr__(self):
        return "<Framework (id='%s', name='%s', url='%s')>" % (self.id, self.name, self.url_name)


class Framework_choice(Base):
    __tablename__ = 'framework_choices'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    framework_id = Column(Integer, ForeignKey('frameworks.id'), nullable=False)
    cereated_at = Column(DateTime(timezone=True),
                         nullable=False, server_default=func.now())

    project = relationship('Project', back_populates='framework_choice')
    framework = relationship('Framework', back_populates='framework_choice')

    def __repr__(self):
        return "<Framework choice (id= '%s', project_id = '%s', framework_id = '%s')>" % (self.id, self.project_id, self.framework_id)
