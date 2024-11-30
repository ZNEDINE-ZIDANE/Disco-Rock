-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 30-11-2024 a las 02:19:38
-- Versión del servidor: 8.0.40
-- Versión de PHP: 8.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rock`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idProducto` int NOT NULL,
  `nombre` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `precio` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `cantidad` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL,
  `categoria` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`idProducto`, `nombre`, `precio`, `cantidad`, `categoria`) VALUES
(17, 'knet', '600', '1002', 'Sin existencias');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `correo` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `clave` varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL,
  `fechareg` datetime NOT NULL,
  `perfil` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_spanish_ci NOT NULL DEFAULT 'U'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `correo`, `clave`, `fechareg`, `perfil`) VALUES
(4, '', '', 'scrypt:32768:8:1$plKxNF9awDUC6WLm$50343bae1dc630bbf6134d5e7f8b4537b5f9f427c8c346e43cbf29b7966bd63caf4e6da6450c163d49595475c09818387f28370607f207badd34cfb19fc2ad18', '2024-11-20 21:20:02', 'A'),
(26, 'ilos', 'kttre@gmail.com', 'scrypt:32768:8:1$FYSlVVawbgy3Mroh$1754f2936f9bdc2ba56eb177ca4e7e104d83cc6da2d2a8d6c169d5f009f4f81a00e9f60693c8805e91ba233cc57b0d882bba4f1ee947e203c7835e7a8b121ace', '2024-11-29 17:09:19', 'A'),
(27, 'knet', 'ke@gmail.com', 'scrypt:32768:8:1$iXKsVjsAjUJddzeq$4db5da0f41d8878d90a2657c7ed79fea4ece907d7ab6163d25d68ff19c772623eac544e9ffc0fcbff2e2d35b57524e6b4cfd36fe64841c7e54415dc1f891793c', '2024-11-29 15:54:34', 'U'),
(28, 'tuputamadretgccghg', 'k111@gmail.com', 'scrypt:32768:8:1$BPAm8VXMfHu9yxla$5ec727ddbfd3d20f06ac4a7f0cae082ca9e4905d3befe412e0e02ed28eec9cd0c6a16cd21438004ba7127040702d471ac64b7138794cb09bf4357d624fe15292', '2024-11-29 16:12:12', 'A'),
(29, 'knet', 'kanet.ochoAAAa19221@alumnos.udg.mx', 'scrypt:32768:8:1$249GMhhMbl0kprWe$e64f846b16c19ddab2547d00881f7b25cfb390c3b6e263d574773edbdaf76be7bc8d62fba4866a23b14f20a5fff904899a883bbfa1ec09c0bc65900721e13c00', '2024-11-29 16:34:06', 'A'),
(30, 'popo', 'kanet.ochoa19221@alumnos.udg.mx', 'scrypt:32768:8:1$y3pCHPlt6M8E81un$0ab7d8ec90e309561204d6909271170d1f64afc436346aef4cb0ce8b1e8bc8012c0c4b467fa0dc3d61b1cba763ff9a00728c5ebd9ec518e90d530d50709c7c91', '2024-11-29 17:12:40', 'U'),
(32, 'popo', 'kanet.ochoas19221@alumnos.udg.mx', 'scrypt:32768:8:1$fmngLDMRZ0qoLgxr$29f98b33031c2759f03c6f380fe3511641746be14b4c17ca5b99e2bb00aa05226a7b82f6f90193bb6f6c4fe25421fd846f3fe2c4f21d3799ef2268c8570f84e0', '2024-11-29 17:13:12', 'U'),
(33, 'tuputamadretgccghg', 'angelasilva@gmail.com', 'scrypt:32768:8:1$UVhmGmOgy5AVp4wn$e35eaeee9296a2eac5345942c29c49eb9cc52ed5e7be30db636af96b67924c6d150586d7c4f19b014f4eecf71eec3d9fe93b192d6855a1b941922163c0c6830c', '2024-11-29 17:31:25', 'U'),
(34, 'tuputamadretgccghg', 'pedro.mayorga11800@alumnos.udg.mx', 'scrypt:32768:8:1$QBzp9QZSW7YBFVSc$d8312ec1cf1200a8e727a0bac134f49f34751f2783fefafac125d7ddda3df6a508e3426b80f5593b38b8004dbc8e57e5b4626d4605455133e59e7d7ddb645c12', '2024-11-29 17:47:48', 'U'),
(36, 'tuputamadretgccghg', 'pedro.mayorga111800@alumnos.udg.mx', 'scrypt:32768:8:1$Vr5CJ09UA3cfIZIc$04f1ce65a9735fe4e6d7e8019d394254f38cf23f1605180b9bf06d6adbd98c586b350591801603f5641f38fa7c914b17e5c1bb7a41141731905a627a449e93cc', '2024-11-29 17:48:09', 'U'),
(37, 'kanet', 'kanet1@gmail.com', 'scrypt:32768:8:1$HMTU9w3uTAgVxhS0$34747cba58bed599b08d5aa66e67161a7212d56d05f96cd1fba9c5b8c968ee45f344a55d768b2d368e120daee03a8409f406cf1b284f5645efae624fce28bd3f', '2024-11-29 18:03:09', 'U');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo_2` (`correo`),
  ADD KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idProducto` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
