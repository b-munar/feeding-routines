# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/feeding-routines

2. 

```bash
docker compose build
docker compose up
```


El servicio de Servicios de terceros.

## 1. Get feeding-routines 

Retorna rutina de alimentacin.

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6150/feeding-routines</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "profiles": [
        {
            "id": "cc8f6ebf-ce9a-4170-af17-5d04c55cd167",
            "meals_per_day": 3,
            "alergies": "Ninguna",
            "health_issues": "Arritmia",
            "time_to_cook": 10
        },
        {
            "id": "3b601709-ff3f-4eec-88fa-6764169b3429",
            "meals_per_day": 3,
            "alergies": "Ninguna",
            "health_issues": "Arritmia",
            "time_to_cook": 10
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>

## 2. Post feeding routines 

Permite realizar creación de rutinas de alimentación.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6150/feeding-routines</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
  {
    "meals_per_day": 3,
    "alergies": "Ninguna",
    "health_issues": "Arritmia",
    "time_to_cook": 10
}
  ```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "id": "3b601709-ff3f-4eec-88fa-6764169b3429",
    "meals_per_day": 3,
    "alergies": "Ninguna",
    "health_issues": "Arritmia",
    "time_to_cook": 10
}
```
</td>
</tr>
</tbody>
</table>

## 3. Get feeding-routines 

Retorna rutina de alimentacion de todos los deportistas. Solo los partners pueden utilizarlo

<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6150/feeding-routines/sportmen</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>N/A</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En caso de exito</td>
<td>

```json
{
    "profiles": [
        {
            "id": "cc8f6ebf-ce9a-4170-af17-5d04c55cd167",
            "meals_per_day": 3,
            "alergies": "Ninguna",
            "health_issues": "Arritmia",
            "time_to_cook": 10
        },
        {
            "id": "3b601709-ff3f-4eec-88fa-6764169b3429",
            "meals_per_day": 3,
            "alergies": "Ninguna",
            "health_issues": "Arritmia",
            "time_to_cook": 10
        }
    ]
}
```
</td>
</tr>
</tbody>
</table>
