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
      "id": "22e7359e-25e2-40f2-9db6-77a43c25e71d",
      "user": "28a3ad77-7d3c-47e3-9c42-858ca3ec5222",
      "meals_per_day": 3,
      "alergies": "Ninguna",
      "health_issues": "Arritmia",
      "time_to_cook": 10,
      "user_info": {
        "sportmen": {
          "name": "",
          "last_name": "",
          "age": 0,
          "weight": 0,
          "height": 0,
          "gender": "",
          "identification_type": "",
          "identification": "",
          "country_birth": "",
          "city_birth": "",
          "country_residence": "",
          "city_residence": "",
          "length_residence": 0,
          "created_at": "0001-01-01T00:00:00Z",
          "updated_at": "0001-01-01T00:00:00Z",
          "sports": null
        }
      }
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
