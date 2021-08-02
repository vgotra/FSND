import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ActorComponent } from './pages/actor/actor.component';
import { ActorsComponent } from './pages/actors/actors.component';
import { MovieComponent } from './pages/movie/movie.component';
import { MoviesComponent } from './pages/movies/movies.component';

const routes: Routes = [
  { path: 'actors', component: ActorsComponent },
  { path: 'actors/:id', component: ActorComponent },
  { path: 'movies', component: MoviesComponent },
  { path: 'movies/:id', component: MovieComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
