import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ActorComponent } from './pages/actor/actor.component';
import { ActorsComponent } from './pages/actors/actors.component';
import { GenreComponent } from './pages/genre/genre.component';
import { GenresComponent } from './pages/genres/genres.component';
import { LanguageComponent } from './pages/language/language.component';
import { LanguagesComponent } from './pages/languages/languages.component';
import { MovieComponent } from './pages/movie/movie.component';
import { MoviesComponent } from './pages/movies/movies.component';

const routes: Routes = [
  { path: 'actors', component: ActorsComponent },
  { path: 'actors/:id', component: ActorComponent },
  { path: 'movies', component: MoviesComponent },
  { path: 'movies/:id', component: MovieComponent },
  { path: 'genres', component: GenresComponent },
  { path: 'genres/:id', component: GenreComponent },
  { path: 'languages', component: LanguagesComponent },
  { path: 'languages/:id', component: LanguageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
