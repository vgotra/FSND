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
import { NotFoundComponent } from './common/components/not-found/not-found.component';
import { AuthGuard } from '@auth0/auth0-angular';
import { TokenComponent } from './pages/token/token.component';

const routes: Routes = [
  { path: '', redirectTo: '/actors', pathMatch: 'full' },
  { path: 'actors', component: ActorsComponent, canActivate: [AuthGuard] },
  { path: 'actors/:id', component: ActorComponent, canActivate: [AuthGuard] },
  { path: 'movies', component: MoviesComponent, canActivate: [AuthGuard] },
  { path: 'movies/:id', component: MovieComponent, canActivate: [AuthGuard] },
  { path: 'genres', component: GenresComponent, canActivate: [AuthGuard] },
  { path: 'genres/:id', component: GenreComponent, canActivate: [AuthGuard] },
  { path: 'languages', component: LanguagesComponent, canActivate: [AuthGuard] },
  { path: 'languages/:id', component: LanguageComponent, canActivate: [AuthGuard] },
  { path: 'token', component: TokenComponent, canActivate: [AuthGuard] },
  { path: '**', component: NotFoundComponent }  // Wildcard route for a 404 page
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
